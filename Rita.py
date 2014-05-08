#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *


import time
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

ASCII_i=65
ASCII_f=90
gap = 150
current_char = ASCII_i

def char_dif(char_n,increment):
	new_char=char_n+increment
	if new_char>ASCII_f:
		new_char=ASCII_i+(new_char-ASCII_f)-1
	if new_char<ASCII_i:
		new_char=ASCII_f+(new_char-ASCII_i)+1
	return new_char
	

def check_button():
	global current_char
	if (GPIO.input(24) == GPIO.HIGH):
		while (GPIO.input(24) == GPIO.HIGH):
			time.sleep(0.01)
		print "Button Pressed."
		current_char=current_char+1
		for i in range(len(letters)):
			w.itemconfig(letters[i],text=chr(char_dif(current_char,i-2)))		
  	master.after(10,check_button)
 

master = Tk()

w = Canvas(master, width=master.winfo_screenwidth(), height=master.winfo_screenheight(),bg='black')
w.pack()
letters=[]

for i in range(5):
	size=100
	color='white'
	if i==2:
		size=140
		color='gold'
	letters.append(w.create_text(master.winfo_screenwidth()/2+gap*(i-2),master.winfo_screenheight()/4,text=chr(char_dif(ASCII_i,i-2)),font=("Times",size),fill=color))

#w.itemconfig(t,text='B')


master.after(10,check_button)
master.mainloop()
