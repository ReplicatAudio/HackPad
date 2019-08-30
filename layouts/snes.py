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
def pressL(lp):
	cf.key_press(lp,'i')
	cf.set_light(lp,{'x':0,'y':5,'rgb':highlight_color})
	cf.set_light(lp,{'x':1,'y':5,'rgb':highlight_color})
def releaseL(lp):
	cf.key_release(lp,'i')
	cf.set_light(lp,{'x':0,'y':5,'rgb':[10,0,10]})
	cf.set_light(lp,{'x':1,'y':5,'rgb':[10,0,10]})

def pressR(lp):
	cf.key_press(lp,'o')
	cf.set_light(lp,{'x':6,'y':5,'rgb':highlight_color})
	cf.set_light(lp,{'x':7,'y':5,'rgb':highlight_color})
def releaseR(lp):
	cf.key_release(lp,'o')
	cf.set_light(lp,{'x':6,'y':5,'rgb':[10,0,10]})
	cf.set_light(lp,{'x':7,'y':5,'rgb':[10,0,10]})


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
	'y':6,
	'r':10,
	'g':10,
	'b':10
})

layout.append({
	'name':'A Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'a',
	'r_arg':'a',
	'x':0,
	'y':7,
	'r':10,
	'g':10,
	'b':10
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
	'r':10,
	'g':10,
	'b':10
})

layout.append({
	'name':'D Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'d',
	'r_arg':'d',
	'x':2,
	'y':7,
	'r':10,
	'g':10,
	'b':10
})

layout.append({
	'name':'N Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'n',
	'r_arg':'n',
	'x':5,
	'y':7,
	'r':0,
	'g':256,
	'b':0
})

layout.append({
	'name':'J Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'j',
	'r_arg':'j',
	'x':6,
	'y':6,
	'r':0,
	'g':0,
	'b':256
})

layout.append({
	'name':'M Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'m',
	'r_arg':'m',
	'x':6,
	'y':8,
	'r':256,
	'g':256,
	'b':0
})

layout.append({
	'name':'K Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'k',
	'r_arg':'k',
	'x':7,
	'y':7,
	'r':256,
	'g':0,
	'b':0
})

layout.append({
	'name':'Enter Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':'enter',
	'r_arg':'enter',
	'x':3,
	'y':8,
	'r':5,
	'g':5,
	'b':5
})

layout.append({
	'name':'; Key',
	'oneShot':False,
	'press':cf.key_press,
	'release':cf.key_release,
	'p_arg':';',
	'r_arg':';',
	'x':4,
	'y':8,
	'r':5,
	'g':5,
	'b':5
})

layout.append({
	'name':'O Key',
	'oneShot':False,
	'press':pressR,
	'release':releaseR,
	'x':6,
	'y':5,
	'r':10,
	'g':0,
	'b':10
})

layout.append({
	'name':'O Key 2',
	'oneShot':False,
	'press':pressR,
	'release':releaseR,
	'x':7,
	'y':5,
	'r':10,
	'g':0,
	'b':10
})

layout.append({
	'name':'I Key',
	'oneShot':False,
	'press':pressL,
	'release':releaseL,
	'x':0,
	'y':5,
	'r':10,
	'g':0,
	'b':10
})

layout.append({
	'name':'I Key 2',
	'oneShot':False,
	'press':pressL,
	'release':releaseL,
	'x':1,
	'y':5,
	'r':10,
	'g':0,
	'b':10
})


