import core_functions as cf
import user_functions as uf

layout = []

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
	'press':uf.open_chrome,
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