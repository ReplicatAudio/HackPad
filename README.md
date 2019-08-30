# HackPad
Use your Novation Launchpad for whatever you can imagine. This essentially turns your device into a 9x9 RGB macro keyboard.

**README NEEDS UPDATE**

Based on [```launchpad_py```](https://github.com/FMMT666/launchpad.py) so this should cover any model available (in theory) but I only have access to an mkII. 

**Inspired by [LPHK](https://github.com/nimaid/LPHK) which is an amazing project, that you may very well find more useful than this. I only wrote this because I prefer to regular python for the pad actions and do not really need a GUI.**

## Setup
```bash
pip install launchpad_py
pip install keyboard
pip install playsound
```
**NOTE**: ```keyboard``` and ```playsound``` are technically optional, but they are required if you want to make use of the ```core_functions``` included with this software.
## Usage
Run with:
```bash
python launch.py
```
### Layout
You layout(s) are stored in the ```layout``` directory. Each file in this directory contains it's own layout as well as any custom functions that you have written for that layout. 

**NOTE:** Specify which layout you want to use in the ```layout.py``` file.

This is where you can setup pad colors and functions. Think of each entry here as an "action" that can be assigned to the launchpad.
```python
layout.append({
    'name':'A Key', # The "friendly" name of the action. Used only for CLI output. 
	'oneShot':False, #Should the action be looped as long as the pad is pressed (False) or just run one time (True)?
	'press':cf.key_press, #The function that should be called when the pad is pressed. This calls 'core_functions.key_press' but it can be any function you want.
	'release':cf.key_release, #The function that should be called when the pad is released. This calls 'core_functions.key_release' but it can be any function you want
	'p_arg':'a', #The argument(s) that should be passed to the press function. Use an array for multiple values. We are pressing the 'a' key here.
	'r_arg':'a', #The argument(s) that should be passed to the press function. Use an array for multiple values. We are releasing the 'a' key here.
	'x':0, #The x coordinate of the pad we are assigning this function to.
	'y':8, #The y coordinate of the pad we are assigning this function to.
	'r':256, # The red RGB value of the pad.
	'g':0, # The green RGB value of the pad.
	'b':0 # The blue RGB value of the pad.
})
```

Not all of the data is required. For instance a pad can have only a release function and no press function which would essentially make it a one-shot. 
```python
	'name': #REQUIRED
	'oneShot':#REQUIRED
	'press': #OPTIONAL
	'release': #OPTIONAL
	'p_arg': #OPTIONAL
	'r_arg': #OPTIONAL
	'x': #REQUIRED
	'y': #REQUIRED
	'r': #REQUIRED
	'g': #REQUIRED
	'b': #REQUIRED
```
There are some core functions provided by this software that can help you get started with writing your own custom layouts. These are basically just wrappers around the ```keyboard``` and ```playsound``` library. You can check them out simply by browsing the ```core/functions.py``` file. 

### User Functions
User functions allow you to add in your own custom functions using any python packages that you would like. There is a simple example in that file to get you started and the last "action" in ```layouts/default.py``` shows how you can assign a user function to the layout.