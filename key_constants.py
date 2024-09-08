LAYOUT_MAP = {
    0x0409: 'English (US)',
    0x0419: 'Russian'
}

LANGS = {
    "Russian": "йцукенгшщзхъфывапролджэячсмитьбю.1234567890-=!\"№;%:?*()_+ёЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,/",
    "English (US)": "qwertyuiop[]asdfghjkl;'zxcvbnm,./1234567890-=!@#$%^&*()_+`~QWERTYUIOP{}ASDFGHJKL:\"ZXCVBNM<>?|"
}

MODIFIER_KEYS = (
    "Key.alt", "Key.alt_l", "Key.alt_r",
    "Key.ctrl", "Key.ctrl_l", "Key.ctrl_r",
    "Key.shift", "Key.shift_l", "Key.shift_r",
    "Key.cmd", "Key.cmd_l", "Key.cmd_r",
    "Key.caps_lock", "Key.delete", "Key.insert",
    "Key.pause", "Key.menu", "Key.scroll_lock"
)

SPECIAL_PRINTING_KEYS = {
    "Key.space": " ",
    "Key.enter": "\n",
    "Key.tab": "\t"
}

NAVIGATION_KEYS = {
    "Key.up": "↑",
    "Key.down": "↓",
    "Key.left": "←",
    "Key.right": "→",
    "Key.page_up": "Pg ↑",
    "Key.page_down": "Pg ↓",
    "Key.home": "Home",
    "Key.end": "End",
    "Key.backspace": "Bs"
}

NUMPAD_KEYS = {
    "Key.numpad0": "Np0",
    "Key.numpad1": "Np1",
    "Key.numpad2": "Np2",
    "Key.numpad3": "Np3",
    "Key.numpad4": "Np4",
    "Key.numpad5": "Np5",
    "Key.numpad6": "Np6",
    "Key.numpad7": "Np7",
    "Key.numpad8": "Np8",
    "Key.numpad9": "Np9",
    "Key.numpad_add": "Np(+)",
    "Key.numpad_subtract": "Np(-)",
    "Key.numpad_multiply": "Np(*)",
    "Key.numpad_divide": "Np(/)",
    "Key.numpad_enter": "Np Enter",
    "Key.numpad_decimal": "Np (.)"
}

SYSTEM_KEYS = {
    "Key.media_volume_mute": "Volume Mute",
    "Key.media_volume_up": "Volume Up",
    "Key.media_volume_down": "Volume Down",
    "Key.media_play_pause": "Play/Pause",
    "Key.media_next": "Next Track",
    "Key.media_previous": "Previous Track",
    "Key.print_screen": "Print Screen",
    "Key.num_lock": "NumLock"
}

NON_PRINTING_KEYS = NAVIGATION_KEYS | NUMPAD_KEYS | SYSTEM_KEYS