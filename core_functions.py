import keyboard
from playsound import playsound
def key_press(key):
    keyboard.press(key)

def key_release(key):
    keyboard.release(key)

def key_tap(key):
    keyboard.send(key)

def play_sound(sound):
    print('Playing sound',sound)
    try:
        playsound(sound)
    except KeyError:
        print('Could not play',sound)

def nothing():
    pass
