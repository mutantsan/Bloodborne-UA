import re
from pathlib import Path
from xml.etree import ElementTree

WITCHY_BND_METADATA = "_witchy-bnd4.xml"
SKIP_LINES = ("%null%", "*", " ", "  ", "   ", "    ", "****", ".", "…", "<?belongMsg?>, ")
SKIP_FILES = [
    "SP_ダイアログ.fmg.xml",
    "キーガイド.fmg.xml",
    "インゲームメニュー.fmg.xml",
    "インゲームメニュー.fmg.xml",
    "SP_メニューテキスト.fmg.xml",
    "ダイアログ.fmg.xml",
    "機種別タグ_win64.fmg.xml",
    "メニュー共通テキスト.fmg.xml",
    "メニュー共通テキスト.fmg.xml",
    WITCHY_BND_METADATA,
]


def main():
    if not check_well_formed():
        raise SystemExit(1)

    find_untranslated_lines()


def check_well_formed() -> bool:
    here = Path(__file__).parent

    ok = True
    for _type in ("menu-msgbnd-dcx", "item-msgbnd-dcx"):
        for file in _get_msg_files(here / _type):
            try:
                ElementTree.parse(file)
            except ElementTree.ParseError as exc:
                print(f"MALFORMED XML: `{file.name}`: {exc}")
                ok = False

    return ok


def find_untranslated_lines():
    here = Path(__file__).parent

    untranslated_lines = []
    translated_lines = []

    for _type in ("menu-msgbnd-dcx", "item-msgbnd-dcx"):
        for file in _get_msg_files(here / _type):
            untrans_lines, trans_lines = _collect_untranslated_(file)

            if untrans_lines:
                print(
                    f"There are {len(untrans_lines)} untranslated lines in `{file.name}`"
                )

            untranslated_lines.extend(untrans_lines)
            translated_lines.extend(trans_lines)

    total = len(untranslated_lines) + len(translated_lines)
    print(
        f"There are {len(untranslated_lines)} untranslated lines in total so far, which is {len(untranslated_lines) / total * 100:.2f}%"
    )


def _get_msg_files(path: Path) -> list[Path]:
    files = []

    for file in path.iterdir():
        if not file.is_file() or file.suffix != ".xml":
            continue

        if file.name in SKIP_FILES:
            continue

        files.append(file)

    return files


def _collect_untranslated_(path: Path) -> tuple[list[str], list[str]]:
    untranslated_lines = []
    translated_lines = []

    entries = ElementTree.parse(path).getroot().find("entries")

    if entries is None:
        return untranslated_lines, translated_lines

    for entry in entries:
        if not entry.text or entry.text in SKIP_LINES:
            continue

        if _has_cyryllic(entry.text):
            translated_lines.append(f"{path.name}: {entry.text}")
            continue

        # e.g en4010
        if re.match(r"\D{2}\d{4}", entry.text):
            continue

        untranslated_lines.append(f"{path.name}: {entry.text}")

    return untranslated_lines, translated_lines


def _has_cyryllic(text: str) -> bool:
    for char in text:
        if 0x0400 <= ord(char) <= 0x04FF:
            return True

    return False


if __name__ == "__main__":
    main()
