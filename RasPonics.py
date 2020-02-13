#the window
from tkinter import *

#define functions
#def myClick():
    #myLabel = Label(root, text="The moon is beautiful, isn't it?", font="none 12 bold", bg='#384048', fg='#e8e8e8' )
    #myLabel.grid(row2, column=3)

def pumpClick():
        pumpClick = Label(root, text="Pump\nON", font="none 12 bold", bg='#708090', fg='green')
        pumpClick.grid(row=2, column=0)
    #elif:
    #def pumpClick():
    #pumpClick = Label(root, text="Pump\nOFF", font="none 12 bold", bg='#708090', fg='red')
    #pumpClick.grid(row=1, column=0)

def fanClick():
        fanClick = Label(root, text="Fan\nON", font="none 12 bold", bg='#708090', fg='green')
        fanClick.grid(row=2, column=1)

def lightClick():
    lightClick = Label(root, text="Light\nON", font="none 12 bold", bg='#708090', fg='green')
    lightClick.grid(row=2, column=2)

def ph1Click():
    ph1Click = Label(root, text="PH UP\nON", font="none 12 bold", bg='#708090', fg='green')
    ph1Click.grid(row=5, column=0)

def ph2Click():
    ph2Click = Label(root, text="PH DWN\nON", font="none 12 bold", bg='#708090', fg='green')
    ph2Click.grid(row=5, column=1)

def resfilClick():
    resfilClick = Label(root, text="Fill\nON", font="none 12 bold", bg='#708090', fg='green')
    resfilClick.grid(row=5, column=2)



root = Tk()
root.title("RasPonics 1.0")
root.configure(bg='#384048')

frame = LabelFrame(root, bg='#384048',padx=50, pady=45)
frame.grid(row=0, column=1, padx=10, pady=10)

frame2 = LabelFrame(root, bg='#384048', padx=150, pady=166)
frame2.grid(row=0, column=0, padx=10, pady=10)

#the widgets
pump = Button(frame, padx=45, pady=40, bg='#708090', fg='#e8e8e8', command=pumpClick)
pump.grid(row=2, column=0)

fan = Button(frame, padx=45, pady=40, bg='#708090', fg='#e8e8e8', command=fanClick)
fan.grid(row=2, column=1)

light = Button(frame, padx=45, pady=40, bg='#708090', fg='#e8e8e8', command=lightClick)
light.grid(row=2, column=2)

ph1 = Button(frame, padx=45, pady=40, bg='#708090', fg='#e8e8e8', command=ph1Click)
ph1.grid(row=5, column=0)
ph2 = Button(frame, padx=45, pady=40, bg='#708090', fg='#e8e8e8', command=ph2Click)
ph2.grid(row=5, column=1)

resfil = Button(frame, padx=45, pady=40, bg='#708090', fg='#e8e8e8', command=resfilClick)
resfil.grid(row=5, column=2)

#gauges

#gauge labels
gauge0 = Label(frame2, text="Gauges\n\n", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge0.grid(row=0, column=1)
gauge1 = Label(frame2, text="Water Flow", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge1.grid(row=1, column=0)
gauge2 = Label(frame2, text="Fill Flow", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge2.grid(row=1, column=1)
gauge3 = Label(frame2, text="PH Level", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge3.grid(row=1, column=2)
gauge4 = Label(frame2, text="Temp", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge4.grid(row=1, column=3)


#Widget Labels
label0 = Label(frame, text="System\nManual Over-Ride\n", font="none 12 bold", bg='#384048', fg='#e8e8e8')
label0.grid(row=0, column=1)
label1 = Label(frame, text="Pump", bg='#384048', fg='#e8e8e8')
label1.grid(row=1, column=0)
label2 = Label(frame, text="Fan", bg='#384048', fg='#e8e8e8')
label2.grid(row=1, column=1)
label3 = Label(frame, text="Light", bg='#384048', fg='#e8e8e8')
label3.grid(row=1, column=2)
label4 = Label(frame, text="\nPH UP", bg='#384048', fg='#e8e8e8')
label4.grid(row=4, column=0)
label5 = Label(frame, text="\nPH Down", bg='#384048', fg='#e8e8e8')
label5.grid(row=4, column=1)
label6 = Label(frame, text="\nReservoir Fill", bg='#384048', fg='#e8e8e8')
label6.grid(row=4, column=2)
#label1 = Label(root, text="")



root.mainloop()
#384048