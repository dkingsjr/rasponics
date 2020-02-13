from tkinter import *


root = Tk()
root.title("RasPonics 1.0")
root.configure(bg='#384048')

frame = LabelFrame(root, bg='#384048', padx=50, pady=45)
frame.grid(row=0, column=1, padx=10, pady=10)

frame2 = LabelFrame(root, bg='#384048', padx=150, pady=166)
frame2.grid(row=0, column=0, padx=10, pady=10)

frame3 = LabelFrame(root, bg='#384048', padx=0, pady=0)
frame3.grid(row=0, column=1, padx=15, pady=15, sticky=E+N)


pump_click_status = True
fan_click_status = True
lightClick_status = True
ph1Click_status = True
ph2Click_status = True
resfilClick_status = True


def pumpClick():
    global pump_click_status
    if pump_click_status:
        pumpClick = Label(frame, text="Pump\nON", font="none 12 bold", bg='#708090', fg='green')
        pumpClick.grid(row=2, column=0)
        pump_click_status = False
    else:
        pumpClick = Label(frame, text="Pump\nOFF", font="none 12 bold", bg='#708090', fg='red')
        pumpClick.grid(row=2, column=0)
        pump_click_status = True


def fanClick():
    global fan_click_status
    if fan_click_status:
        fanClick = Label(frame, text="Fan\nON", font="none 12 bold", bg='#708090', fg='green')
        fanClick.grid(row=2, column=1)
        fan_click_status = False
    else:
        fanClick = Label(frame, text="Fan\nOFF", font="none 12 bold", bg='#708090', fg='red')
        fanClick.grid(row=2, column=1)
        fan_click_status = True


def lightClick():
    global lightClick_status
    if lightClick_status:
        lightClick = Label(frame, text="Light\nON", font="none 12 bold", bg='#708090', fg='green')
        lightClick.grid(row=2, column=2)
        lightClick_status = False
    else:
        lightClick = Label(frame, text="Light\nOFF", font="none 12 bold", bg='#708090', fg='red')
        lightClick.grid(row=2, column=2)
        lightClick_status = True


def ph1Click():
    global ph1Click_status
    if ph1Click_status:
        ph1Click = Label(frame, text="PH UP\nON", font="none 12 bold", bg='#708090', fg='green')
        ph1Click.grid(row=5, column=0)
        ph1Click_status = False
    else:
        ph1Click = Label(frame, text="PH UP\nOFF", font="none 12 bold", bg='#708090', fg='red')
        ph1Click.grid(row=5, column=0)
        ph1Click_status = True


def ph2Click():
    global  ph2Click_status
    if ph2Click_status:
        ph2Click = Label(frame, text="PH DWN\nON", font="none 12 bold", bg='#708090', fg='green')
        ph2Click.grid(row=5, column=1)
        ph2Click_status = False
    else:
        ph2Click = Label(frame, text="PH DWN\nOFF", font="none 12 bold", bg='#708090', fg='red')
        ph2Click.grid(row=5, column=1)
        ph2Click_status = True


def resfilClick():
    global resfilClick_status
    if resfilClick_status:
        resfilClick = Label(frame, text="Fill\nON", font="none 12 bold", bg='#708090', fg='green')
        resfilClick.grid(row=5, column=2)
        resfilClick_status = False
    else:
        resfilClick = Label(frame, text="Fill\nOFF", font="none 12 bold", bg='#708090', fg='red')
        resfilClick.grid(row=5, column=2)
        resfilClick_status = True


# Buttons
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


# Close GUI
close = Button(frame3, padx=0, pady=0, fg='black', highlightbackground='red', highlightcolor='red', command=root.destroy)
close.grid(row=0, column=1)
close.config(text='X', height=1, width=1, relief=RAISED)


# gauge labels
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


# Widget Labels
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

root.mainloop()
