import keyboard
from playsound import playsound
def key_press(lp, key):
    keyboard.press(key)

def key_release(lp, key):
    keyboard.release(key)

def key_tap(lp, key):
    keyboard.send(key)

def set_light(lp, data):
    print(data['x'])
    lp.LedCtrlXY(data['x'],data['y'],data['rgb'][0],data['rgb'][1],data['rgb'][2])

def play_sound(lp, sound):
    print('Playing sound',sound)
    try:
        playsound(sound)
    except KeyError:
        print('Could not play',sound)

def nothing():
    pass
