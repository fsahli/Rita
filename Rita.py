from Tkinter import *

import time
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

ASCII_i=65
ASCII_f=90

def check_button():
	if (GPIO.input(18) == GPIO.LOW):
		labelText.set("Button Pressed.")
	else:
		labelText.set("")
  	master.after(10,check_button)
 

master = Tk()

w = Canvas(master, width=master.winfo_screenwidth(), height=master.winfo_screenheight(),bg='black')
w.pack()
t=w.create_text(400,400,text='A',font=("Times",140),fill='white')

w.updateconfig(t,text='B')


master.after(10,check_button)
master.mainloop()
