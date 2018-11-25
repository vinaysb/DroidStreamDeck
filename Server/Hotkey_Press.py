import keyboard
import settings


def Hotkey(value):
    settings._unpickling()
    if value in settings.options:
        hkey = settings.options[value]
        keyboard.press_and_release(hkey)
    else:
        print('Not bound to anything, please bind button' + value)
