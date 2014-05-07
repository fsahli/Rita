from Tkinter import *

master = Tk()

w = Canvas(master, width=800,height=600,bg='black')
w.pack()
t=w.create_text(400,400,text='A',font=("Times",140),fill='white')
