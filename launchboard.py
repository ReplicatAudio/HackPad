import sys

try:
	import launchpad_py as launchpad
except ImportError:
	try:
		import launchpad
	except ImportError:
	    sys.exit("ERROR: loading launchpad.py failed. Make sure you followed the setup steps!")

import random
import pygame
from pygame import time

from user.layout import layout

import threading
import time

def main():
	lp = launchpad.LaunchpadMk2()
	
	init(lp)
	setLayout(lp)
	pressed = []

	while True:
		but = lp.ButtonStateXY()
		if but != []:
			highlightPressed(lp,but)
			if(but[2]==127):#pressed
				pressed.append(but)
			else:
				removal = 0
				for i in range(len(pressed)):
					if([pressed[i][0],pressed[i][1]]==[but[0],but[1]]):
						removal = i
				try:
					del pressed[removal]
					releaseFunction(lp,but)
				except IndexError:
					pass
				
		if(pressed!=[]):			
			print(pressed)
		pressedFunctions(lp,pressed)
		time.sleep(0.025)

def releaseFunction(lp,but):
	print("released: ",but)
	for pad in layout:
		if([pad['x'],pad['y']]==[but[0],but[1]]):
			print("Running ",pad['name'],"released.")
			try:
				thread = threading.Thread(target=pad['release'], args=[pad['r_arg']])
				thread.start()
			except KeyError:
				try:
					thread = threading.Thread(target=pad['press'], args=())
					thread.start()
				except KeyError:
					print("Warning: Can not run this pad's (",pad['name'],") release function. Maybe it doesn't even have one...")
			

def pressedFunctions(lp,pressed):
	for pad in layout:
		for i in range(len(pressed)):
			removal = -1
			if([pad['x'],pad['y']]==[pressed[i][0],pressed[i][1]]):
				print("Running ",pad['name'],"pressed.")
				try:
					thread = threading.Thread(target=pad['press'], args=[pad['p_arg']])
					thread.start()
				except KeyError:
					try:
						thread = threading.Thread(target=pad['press'], args=())
						thread.start()
					except KeyError:
						print("Warning: Can not run this pad's (",pad['name'],") press function. Maybe it doesn't even have one...")
				
				if(pad['oneShot']==True):
					removal = i
			if(removal!=-1):
				print(pad['name'],"was a one shot. Simulating release now, but not activating a release function.")
				# No need to worry about release for a one shot
				del pressed[removal]
			
def init(lp):
	# open the first Launchpad Mk2
	if lp.Open( 0, "mk2" ):
		print( " - Launchpad Mk2: OK" )
	else:
		print( " - Launchpad Mk2: ERROR" )
		return
	# Clear the buffer because the Launchpad remembers everything
	lp.ButtonFlush()
	lp.Reset() # turn all LEDs off

def setLayout(lp):
	for pad in layout:
		lp.LedCtrlXY(pad['x'],pad['y'],pad['r'],pad['g'],pad['b'])

def highlightPressed(lp,but):
	#print(" event: ", but )
	hc = [80,80,80] #highlight color
	if(but[2]==127):
		lp.LedCtrlXY(but[0],but[1],hc[0],hc[1],hc[2])
	else:
		inLayout = False
		for pad in layout:
			if([pad['x'],pad['y']]==[but[0],but[1]]):
				inLayout = True
				lp.LedCtrlXY(but[0],but[1],pad['r'],pad['g'],pad['b'])
		if(inLayout==False):	
			lp.LedCtrlXY(but[0],but[1],0,0,0)

if __name__ == '__main__':
	main()