import subprocess
import shutil
from pathlib import Path


WITCHY_BND_EXE = "/mnt/d/apps/WitchyBND/WitchyBND.exe"
WITCHY_BND_METADATA = "_witchy-bnd4.xml"
BLOODBORNE_PATH = "/mnt/d/apps/shadps4 diegolix29/games/CUSA03173/dvdroot_ps4/msg/rusru/"


def main():
    copy_files_to_pack_folder()
    pack_translate_files()
    replace_translation_files()


def copy_files_to_pack_folder() -> None:
    here = Path(__file__).parent
    menu_msg_files = here / "menu-msgbnd-dcx"
    item_msg_files = here / "item-msgbnd-dcx"

    pack_folder = here / "pack"

    shutil.rmtree(pack_folder, ignore_errors=True)

    shutil.copytree(menu_msg_files, pack_folder / "menu-msgbnd-dcx")
    shutil.copytree(item_msg_files, pack_folder / "item-msgbnd-dcx")


def pack_translate_files() -> None:
    """Pack all translated files xml -> fmg -> dcx"""
    subprocess.run([WITCHY_BND_EXE] + get_msg_files("menu"))
    subprocess.run([WITCHY_BND_EXE] + get_msg_files("item"))

    here = Path(__file__).parent

    drop_xml_files()

    subprocess.run([WITCHY_BND_EXE, here / "pack" / "menu-msgbnd-dcx"])
    subprocess.run([WITCHY_BND_EXE, here / "pack" / "item-msgbnd-dcx"])


def get_msg_files(_type: str) -> list[Path]:
    """Get paths to all xml files in menu and item folders

    Args:
        _type (str): "menu" or "item"

    Returns:
        list of paths to xml files
    """
    if _type not in ["menu", "item"]:
        raise ValueError("type must be 'menu' or 'item'")

    here = Path(__file__).parent
    menu_msg_files = here / "pack" / f"{_type}-msgbnd-dcx"

    files = []

    for file in menu_msg_files.iterdir():
        if not file.is_file() or file.suffix != ".xml":
            continue

        # this file is created by WitchyBND after unpacking
        if file.name == WITCHY_BND_METADATA:
            continue

        files.append(file)

    return files


def drop_xml_files() -> None:
    """Remove all xml files from pack folder

    We don't need them, because we already packed them into FMG
    """
    here = Path(__file__).parent

    menu_msg_files = here / "pack" / "menu-msgbnd-dcx"
    item_msg_files = here / "pack" / "item-msgbnd-dcx"

    for file in menu_msg_files.iterdir():
        if file.name == WITCHY_BND_METADATA:
            continue

        if file.suffix == ".xml":
            file.unlink()

    for file in item_msg_files.iterdir():
        if file.name == WITCHY_BND_METADATA:
            continue

        if file.suffix == ".xml":
            file.unlink()


def replace_translation_files() -> None:
    """Replace original files with translated ones"""
    here = Path(__file__).parent

    menu_msg_files = here / "pack" / "menu.msgbnd.dcx"
    item_msg_files = here / "pack" / "item.msgbnd.dcx"

    bb_path = Path(BLOODBORNE_PATH)

    # remove old files
    (bb_path / "menu.msgbnd.dcx").unlink(missing_ok=True)
    (bb_path / "item.msgbnd.dcx").unlink(missing_ok=True)

    # copy new files
    shutil.copy(menu_msg_files, bb_path)
    shutil.copy(item_msg_files, bb_path)


if __name__ == "__main__":
    main()
