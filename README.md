# HackPad
Allows you to easily "hack" your Novation Launchpad and use it for whatever you can imagine. This essentially turns your device into fully "python-scriptable" a 9x9 RGB macro keyboard.

<img src="https://i.imgur.com/u6bi6ev.jpg" width="256px">

Based on [```launchpad_py```](https://github.com/FMMT666/launchpad.py) so this should cover any model available (in theory) but I only have access to an mkII. 

**Inspired by [LPHK](https://github.com/nimaid/LPHK) which is an amazing project, that you may very well find more useful than this.** 

# Setup
```bash
pip install launchpad_py
pip install keyboard
pip install mouse
pip install playsound
```
**NOTE**: ```keyboard```,```mouse``` and ```playsound``` are technically optional, but they are required if you want to make use of the ```core_functions``` included with this software.
# Usage
Run with:
```bash
python launch.py
```
## Layout
You layout(s) are stored in the ```layout``` directory. Each file in this directory contains it's own layout as well as any custom functions that you have written for that layout. Layouts each contain their own macro/hotkey presets for the launchpad. 

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

## User Functions
User functions allow you to add in your own custom functions using any python packages that you would like. There is a simple example in that file to get you started and the last "action" in ```layouts/default.py``` shows how you can assign a user function to the layout. Essentially you just assign it to the value of ```pressed``` or ```released``` for the desired pad in your layout.

**NOTE:** Each user function will have the ```lp``` argument passed to it, so make sure that your custom functions expect that as the the first argument. This means you need to set ```lp``` as the first parameter of your custom function even if you don;t intend on using it. (This might change if I can get around requiring this.)

Example:
```python
def your_custom_function(lp,your_data):
    # Do Something!
```

## Interacting With The Launchpad through User Functions

The ```lp``` argument (representing the Launchpad object) is automatically passed to each custom user function (as well as the core functions). Because of this, every user function has full access to the Launchpad object, and therefor full access to everything you can do with [```launchpad_py```](https://github.com/FMMT666/launchpad.py). There is also a core function that allows you to set the color of a specific light. More core functions might be added later to help deal with setting the LED colors, but for now it's best to just hook into the Launchpad object and do what you need to do in a custom function. 
