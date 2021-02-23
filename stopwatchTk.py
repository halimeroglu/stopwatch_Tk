import time
from tkinter import *

root  = Tk()
root.geometry('350x350')
root.title('Stopwatch')
root.config(bg='#ffbe76')


#create variables
split_second = StringVar()
second = StringVar()
minute = StringVar()

#create default values
split_second.set("00")
second.set("00")
minute.set("00")

#functions
def start_stopwatch():
    t = int(minute.get()) * 60 + int(second.get()) + int(split_second.get()) / 60
    while t > -1:
        secs,s_secs = divmod(t,60)

        mins = 0
        if mins > 60:
            mins,secs = divmod(mins,60)
        split_second.set("{}".format(s_secs))
        second.set("{}".format(secs))
        minute.set("{}".format(mins))

        time.sleep(1/60)
        root.update()
        t += 1
def stop_stopwach():
    time.sleep(10 * 60)


#widgets
title_label = Label(root,text="Stopwatch",fg="#130f40",bg="#ffbe76",font=("Arial",28)).place(x=80,y=30)
minute_entry = Entry(root,textvariable=minute,width=3).place(x=110,y=120)
lbl_1 = Label(root,text=":",fg="#130f40",bg="#ffbe76",font=('Arial',14)).place(x=130,y=120)
second_entry = Entry(root,textvariable=second,width=3).place(x=150,y=120)
lbl_2 = Label(root,text=":",fg="#130f40",bg="#ffbe76",font=('Arial',14)).place(x=170,y=120)
s_second_entry = Entry(root,textvariable=split_second,width=3).place(x=190,y=120)
start_button = Button(root,text="Start",width=10,fg="#130f40",font=('Arial',10),command=start_stopwatch).place(x=120,y=170)
stop_button = Button(root,text="Stop",width=10,fg="#130f40",font=('Arial',10),command=stop_stopwach).place(x=120,y=210)


root.mainloop()