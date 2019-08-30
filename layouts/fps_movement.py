##                       ##
## Import Core Functions ##
##                       ##
import core.functions as cf
##                       ##
## Highlight Options     ##
##                       ##
highlight_color = [256,256,256] #RGB
highlight_empty = False
##                  ##
## Custom Functions ##
##                  ##
import mouse
sense = 50
def mouse_right(lp):
    mouse.move(sense,0,False,0)
def mouse_left(lp):
    mouse.move(-sense,0,False,0)
def mouse_up(lp):
    mouse.move(0,-sense,False,0)
def mouse_down(lp):
    mouse.move(0,sense,False,0)
def mouse_rclick_down(lp):
    mouse.press(button='right')
def mouse_rclick_up(lp):
    mouse.release(button='right')
def mouse_lclick_down(lp):
    mouse.press(button='left')
def mouse_lclick_up(lp):
    mouse.release(button='left')

def press_space(lp):
    cf.key_press(lp,'space')
    cf.set_light(lp,{'x':4,'y':8,'rgb':highlight_color})
    cf.set_light(lp,{'x':5,'y':8,'rgb':highlight_color})
    cf.set_light(lp,{'x':6,'y':8,'rgb':highlight_color})
def release_space(lp):
    cf.key_release(lp,'space')
    cf.set_light(lp,{'x':4,'y':8,'rgb':[256,0,0]})
    cf.set_light(lp,{'x':5,'y':8,'rgb':[256,0,0]})
    cf.set_light(lp,{'x':6,'y':8,'rgb':[256,0,0]})
##                  ##
## Layout           ##
##                  ##
layout = []

layout.append({
	'name':'W Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'w',
	'r_arg':'w',
	'x':3,
	'y':5,
	'r':256,
	'g':0,
	'b':0
})

layout.append({
	'name':'A Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'a',
	'r_arg':'a',
	'x':2,
	'y':6,
	'r':256,
	'g':0,
	'b':0
})

layout.append({
	'name':'S Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'s',
	'r_arg':'s',
	'x':3,
	'y':6,
	'r':256,
	'g':0,
	'b':0
})

layout.append({
	'name':'D Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'d',
	'r_arg':'d',
	'x':4,
	'y':6,
	'r':256,
	'g':0,
	'b':0
})

layout.append({
	'name':'E Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'e',
	'r_arg':'e',
	'x':4,
	'y':5,
	'r':100,
	'g':256,
	'b':10
})

layout.append({
	'name':'Q Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'Q',
	'r_arg':'Q',
	'x':2,
	'y':5,
	'r':10,
	'g':0,
	'b':10
})

layout.append({
	'name':'Shift Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'shift',
	'r_arg':'shift',
	'x':1,
	'y':6,
	'r':10,
	'g':10,
	'b':100
})

layout.append({
	'name':'CTRL Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'ctrl',
	'r_arg':'ctrl',
	'x':0,
	'y':6,
	'r':10,
	'g':100,
	'b':256
})

layout.append({
	'name':'F Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'f',
	'r_arg':'f',
	'x':5,
	'y':6,
	'r':100,
	'g':10,
	'b':10
})

layout.append({
	'name':'C Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'c',
	'r_arg':'c',
	'x':1,
	'y':7,
	'r':10,
	'g':100,
	'b':10
})

layout.append({
	'name':'V Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'v',
	'r_arg':'v',
	'x':5,
	'y':7,
	'r':10,
	'g':0,
	'b':10
})

layout.append({
	'name':'B Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'B',
	'r_arg':'B',
	'x':4,
	'y':7,
	'r':0,
	'g':10,
	'b':10
})

layout.append({
	'name':'1 Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'1',
	'r_arg':'1',
	'x':0,
	'y':4,
	'r':10,
	'g':10,
	'b':10
})

layout.append({
	'name':'2 Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'2',
	'r_arg':'2',
	'x':1,
	'y':4,
	'r':10,
	'g':10,
	'b':10
})

layout.append({
	'name':'3 Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'3',
	'r_arg':'3',
	'x':2,
	'y':4,
	'r':10,
	'g':10,
	'b':10
})

layout.append({
	'name':'4 Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'4',
	'r_arg':'4',
	'x':3,
	'y':4,
	'r':10,
	'g':10,
	'b':10
})

layout.append({
	'name':'5 Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'5',
	'r_arg':'5',
	'x':4,
	'y':4,
	'r':10,
	'g':10,
	'b':10
})

layout.append({
	'name':'6 Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'6',
	'r_arg':'6',
	'x':0,
	'y':3,
	'r':5,
	'g':5,
	'b':5
})

layout.append({
	'name':'7 Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'7',
	'r_arg':'7',
	'x':1,
	'y':3,
	'r':5,
	'g':5,
	'b':5
})

layout.append({
	'name':'8 Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'8',
	'r_arg':'8',
	'x':2,
	'y':3,
	'r':5,
	'g':5,
	'b':5
})

layout.append({
	'name':'9 Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'9',
	'r_arg':'9',
	'x':3,
	'y':3,
	'r':5,
	'g':5,
	'b':5
})

layout.append({
	'name':'0 Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'0',
	'r_arg':'0',
	'x':4,
	'y':3,
	'r':5,
	'g':5,
	'b':5
})

layout.append({
	'name':'Mouse Right',
	'oneShot':False,
	'press':mouse_right,
	'x':7,
	'y':4,
	'r':50,
	'g':50,
	'b':50
})
layout.append({
	'name':'Mouse Left',
	'oneShot':False,
	'press':mouse_left,
	'x':5,
	'y':4,
	'r':50,
	'g':50,
	'b':50
})
layout.append({
	'name':'Mouse Up',
	'oneShot':False,
	'press':mouse_up,
	'x':6,
	'y':3,
	'r':50,
	'g':50,
	'b':50
})
layout.append({
	'name':'Mouse Down',
	'oneShot':False,
	'press':mouse_down,
	'x':6,
	'y':5,
	'r':50,
	'g':50,
	'b':50
})

layout.append({
	'name':'Mouse R Click',
	'oneShot':False,
	'press':mouse_rclick_down,
    'release':mouse_rclick_up,
	'x':8,
	'y':5,
	'r':50,
	'g':256,
	'b':50
})
layout.append({
	'name':'Mouse L Click',
	'oneShot':False,
	'press':mouse_lclick_down,
    'release':mouse_lclick_up,
	'x':8,
	'y':4,
	'r':256,
	'g':0,
	'b':0
})


layout.append({
	'name':'Space Key',
	'oneShot':False,
	'press':press_space,
	'release':release_space,
	'x':5,
	'y':8,
	'r':256,
	'g':0,
	'b':0
})

layout.append({
	'name':'Space Key 2',
	'oneShot':False,
	'press':press_space,
	'release':release_space,
	'x':4,
	'y':8,
	'r':256,
	'g':0,
	'b':0
})

layout.append({
	'name':'Space Key 3',
	'oneShot':False,
	'press':press_space,
	'release':release_space,
	'x':6,
	'y':8,
	'r':256,
	'g':0,
	'b':0
})