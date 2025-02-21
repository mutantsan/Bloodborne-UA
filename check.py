import re
from pathlib import Path

import xml.etree.ElementTree as ET


WITCHY_BND_METADATA = "_witchy-bnd4.xml"

SKIP_FILES = [
    "死因.fmg.xml",
    "アクセサリうんちく.fmg.xml",
    "魔法名.fmg.xml",
    "アクセサリ説明.fmg.xml",
    "アクセサリ名.fmg.xml",
    "防具名.fmg.xml",
    "防具説明.fmg.xml",
    "武器説明.fmg.xml",
    "メニューその他.fmg.xml",
    "テキスト表示用タグ一覧.fmg.xml",
    "一行ヘルプ.fmg.xml",
    "SP_システムメッセージ_win64.fmg.xml",
    "魔法うんちく.fmg.xml",
    "魔法説明.fmg.xml",
    "魔石接頭語.fmg.xml",
    "機種別タグ_win64.fmg.xml",
    "SP_キーガイド.fmg.xml",
    "ムービー字幕.fmg.xml",
    WITCHY_BND_METADATA
]

def main():
    find_untranslated_lines()


def find_untranslated_lines():
    here = Path(__file__).parent

    untranslated_lines = []

    for _type in ("menu-msgbnd-dcx", "item-msgbnd-dcx"):
        for file in _get_msg_files(here / _type):
            lines = _collect_untranslated_(file)

            print(f"There are {len(lines)} untranslated lines in {file.name}")

            untranslated_lines.extend(lines)


def _get_msg_files(path: Path) -> list[Path]:
    files = []

    for file in path.iterdir():
        if not file.is_file() or file.suffix != ".xml":
            continue

        if file.name in SKIP_FILES:
            continue

        files.append(file)

    return files


def _collect_untranslated_(path: Path) -> list[str]:
    lines = []
    skip_lines = ("%null%", "*", " ")

    entries = ET.parse(path).getroot().find("entries")

    if entries is None:
        return lines

    for entry in entries:
        if not entry.text or entry.text in skip_lines or _has_cyryllic(entry.text):
            continue

        # e.g en4010
        if re.match(r"\D{2}\d{4}", entry.text):
            continue

        lines.append(f"{path.name}: {entry.text}")

    return lines


def _has_cyryllic(text: str) -> bool:
    for char in text:
        if 0x0400 <= ord(char) <= 0x04FF:
            return True

    return False


if __name__ == "__main__":
    main()
