#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *


import time, os
import RPi.GPIO as GPIO

green_pin = 17
white_pin = 23
red_pin = 25
off_pin = 24
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(green_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(white_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(red_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(off_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

ASCII_i=65
ASCII_f=90
gap = 150
current_char = ASCII_i
words=""

red_state = GPIO.HIGH
white_state = GPIO.HIGH
green_state = GPIO.HIGH
def char_dif(char_n,increment):
	new_char=char_n+increment
	if new_char>ASCII_f:
		new_char=ASCII_i+(new_char-ASCII_f)-1
	if new_char<ASCII_i:
		new_char=ASCII_f+(new_char-ASCII_i)+1
	return new_char
	

def check_button():
	global current_char
	global words
	global red_state
	global green_state
	global white_state

	if (red_state == GPIO.LOW):
		while (GPIO.input(red_pin) == GPIO.LOW):
			time.sleep(0.01)
	else:
		if (GPIO.input(red_pin) == GPIO.LOW):
			counter = 0
			while (GPIO.input(red_pin) == GPIO.LOW and counter<200):
				time.sleep(0.01)
				counter+=1
				print counter
			print "Button Pressed."
			if counter<200:
				print "entreif"
				current_char=char_dif(current_char,1)
				for i in range(len(letters)):
					w.itemconfig(letters[i],text=chr(char_dif(current_char,i-2)))		
			else:
				print "entrelese"
				words+=" "
				w.itemconfig(words_display,text=words)		

	if (white_state == GPIO.LOW): 
		while (GPIO.input(white_pin) == GPIO.LOW):
			time.sleep(0.01)
	else:
		if (GPIO.input(white_pin) == GPIO.LOW):
			counter = 0
			while (GPIO.input(white_pin) == GPIO.LOW and counter<200):
				time.sleep(0.01)
				counter+=1
			if counter<200:
				words+=chr(current_char)
				w.itemconfig(words_display,text=words)		
			else:
				words=""
				w.itemconfig(words_display,text=words)		
	if (green_state == GPIO.LOW):
		while (GPIO.input(green_pin) == GPIO.LOW):
			time.sleep(0.01)
	else:
		if (GPIO.input(green_pin) == GPIO.LOW):
			counter = 0
			while (GPIO.input(green_pin) == GPIO.LOW and counter<200):
				time.sleep(0.01)
				counter+=1
			if counter<200:
				current_char=char_dif(current_char,-1)
				for i in range(len(letters)):
					w.itemconfig(letters[i],text=chr(char_dif(current_char,i-2)))		
			else:
				words=words[0:-1]
				w.itemconfig(words_display,text=words)		
	white_state = GPIO.input(white_pin)
	green_state = GPIO.input(green_pin)
	red_state = GPIO.input(red_pin)

	if (GPIO.input(off_pin) == GPIO.HIGH):
		os.system("sudo shutdown -h now")

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

words_display=w.create_text(master.winfo_screenwidth()/2,master.winfo_screenheight()/2,text=words,font=("Times",80),fill='white',width=master.winfo_screenwidth(),anchor='n')

master.after(10,check_button)
master.mainloop()
