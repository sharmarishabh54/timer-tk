from tkinter import *
import time

import pygame





h=Tk()

h.title("TIMER")
h.geometry("340x300")


frame=Frame(h)
frame2=Frame(h)
frame3=Frame(h)
label1=Label(frame,text='Timer',font="times 30")

icon = PhotoImage(file='clock1.gif')
h.tk.call('wm', 'iconphoto', h._w, icon)

second=Label(frame2,text='time',font='times 20')
second.grid(row=0,sticky=E)
entry=Entry(frame2)

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
screen = pygame.display.set_mode((640, 480))

def playNotificationSound2():
    pygame.mixer.music.load("final.mp3")
    pygame.mixer.music.play()


def d1():
    a=int(entry.get())
    
    for i in range(a):
        b=(a-i)
        time.sleep(1)
        
    playNotificationSound2()    
    sn=("TIME IS UP ")
    txt.insert(0.0,sn)


clock=PhotoImage(file="alarm_clock.gif")

pic=Label(frame,image=clock)

button=Button(frame2,text='set',font='times 14',bg='darkgray',fg='midnightblue',command=d1)



txt=Text(frame3,width=50, height=5, wrap=WORD)

txt.grid(row=5,columnspan=2,sticky=W)


frame.pack()
frame2.pack(side=LEFT)
frame3.pack(side=BOTTOM)
second.pack(side=LEFT)
entry.pack(side=LEFT)
pic.pack()
button.pack(side=BOTTOM,padx=4,pady=4)
label1.pack()
h.mainloop()
