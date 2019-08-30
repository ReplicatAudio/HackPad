##                       ##
## Import Core Functions ##
##                       ##
import core.functions as cf
##                  ##
## Custom Functions ##
##                  ##
import subprocess
def open_chrome():
    subprocess.run(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"])
##                       ##
## Highlight Options     ##
##                       ##
highlight_color = [0,0,256] #RGB
highlight_empty = True
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
	'x':1,
	'y':7,
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
	'x':0,
	'y':8,
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
	'x':1,
	'y':8,
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
	'x':2,
	'y':8,
	'r':256,
	'g':0,
	'b':0
})

layout.append({
	'name':'Enter Key',
	'oneShot':True,
	'press':cf.key_tap,
	'p_arg':'enter',
	'r_arg':'enter',
	'x':2,
	'y':2,
	'r':256,
	'g':0,
	'b':0
})

layout.append({
	'name':'Woosh Sound',
	'oneShot':True,
	'press':cf.play_sound,
	'p_arg':"sfx/woosh.wav",
	'x':3,
	'y':5,
	'r':256,
	'g':0,
	'b':0
})

layout.append({
	'name':'Open Chrome',
	'oneShot':True,
	'press':open_chrome,
	'x':7,
	'y':3,
	'r':0,
	'g':256,
	'b':0
})

layout.append({
	'name':'Bug Test',
	'oneShot':False,
	'x':1,
	'y':1,
	'r':0,
	'g':0,
	'b':256
})

layout.append({
	'name':'Change Light',
	'oneShot':False,
	'press':cf.set_light,
	'p_arg':{'x':6,'y':7,'rgb':[0,256,0]},
	'x':6,
	'y':8,
	'r':0,
	'g':100,
	'b':100
})

layout.append({
	'name':'Change Light 2',
	'oneShot':True,
	'press':cf.set_light,
	'p_arg':{'x':7,'y':7,'rgb':[0,256,0]},
	'x':7,
	'y':8,
	'r':0,
	'g':100,
	'b':100
})

layout.append({
	'name':'Change Light 3',
	'oneShot':False,
	'press':cf.set_light,
	'p_arg':{'x':6,'y':8,'rgb':[50,10,50]},
	'x':6,
	'y':7,
	'r':50,
	'g':10,
	'b':100
})

