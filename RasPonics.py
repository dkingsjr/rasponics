from tkinter import *
import sys


pump_click_status = True


def pumpClick():
    global pump_click_status
    if pump_click_status:
        pumpClick = Label(frame4, text="Pump\nON", font="none 12 bold", bg='#708090', fg='green')
        pumpClick.grid(row=2, column=0)
        pump_click_status = False
    else:
        pumpClick = Label(frame4, text="Pump\nOFF", font="none 12 bold", bg='#708090', fg='red')
        pumpClick.grid(row=2, column=0)
        pump_click_status = True


fan_click_status = True


def fanClick():
    global fan_click_status
    if fan_click_status:
        fanClick = Label(frame4, text="Fan\nON", font="none 12 bold", bg='#708090', fg='green')
        fanClick.grid(row=2, column=1)
        fan_click_status = False
    else:
        fanClick = Label(frame4, text="Fan\nOFF", font="none 12 bold", bg='#708090', fg='red')
        fanClick.grid(row=2, column=1)
        fan_click_status = True


light_click_status = True


def lightClick():
    global light_click_status
    if light_click_status:
        lightClick = Label(frame4, text="Light\nON", font="none 12 bold", bg='#708090', fg='green')
        lightClick.grid(row=2, column=2)
        light_click_status = False
    else:
        lightClick = Label(frame4, text="Light\nOFF", font="none 12 bold", bg='#708090', fg='red')
        lightClick.grid(row=2, column=2)
        light_click_status = True


ph1_click_status = True


def ph1Click():
    global ph1_click_status
    if ph1_click_status:
        ph1Click = Label(frame4, text="PH UP\nON", font="none 12 bold", bg='#708090', fg='green')
        ph1Click.grid(row=5, column=0)
        ph1_click_status = False
    else:
        ph1Click = Label(frame4, text="PH UP\nOFF", font="none 12 bold", bg='#708090', fg='red')
        ph1Click.grid(row=5, column=0)
        ph1_click_status = True


ph2_click_status = True


def ph2Click():
    global ph2_click_status
    if ph2_click_status:
        ph2Click = Label(frame4, text="PH Down\nON", font="none 12 bold", bg='#708090', fg='green')
        ph2Click.grid(row=5, column=1)
        ph2_click_status = False
    else:
        ph2Click = Label(frame4, text="PH Down\nOFF", font="none 12 bold", bg='#708090', fg='red')
        ph2Click.grid(row=5, column=1)
        ph2_click_status = True


resfil_click_status = True


def resfilClick():
    resfilClick = Label(frame4, text="Fill\nON", font="none 12 bold", bg='#708090', fg='green')
    resfilClick.grid(row=5, column=2)
    global resfil_click_status
    if resfil_click_status:
        resfilClick = Label(frame4, text="Fill\nON", font="none 12 bold", bg='#708090', fg='green')
        resfilClick.grid(row=5, column=2)
        resfil_click_status = False
    else:
        resfilClick = Label(frame4, text="Fill\nOFF", font="none 12 bold", bg='#708090', fg='red')
        resfilClick.grid(row=5, column=2)
        resfil_click_status = True

#the window
root = Tk()
root.title("RasPonics 1.0")
root.configure(bg='#384048')
#window dimensions(auto size)
RWidth=root.winfo_screenwidth()
RHeight=root.winfo_screenheight()
root.geometry(("%dx%d")%(RWidth,RHeight))

#Frames
mainframe = LabelFrame(root, bg='#384048', padx=10, pady=10, relief=SUNKEN)
mainframe.pack(fill="both", expand=True, padx=10, pady=10)

frame = LabelFrame(mainframe, bg='#384048', padx=10, pady=10, relief=RAISED)
frame.grid(row=0, column=0, padx=5, pady=5)

frame2 = LabelFrame(mainframe, bg='#384048', padx=10, pady=10, relief=RAISED)
frame2.grid(row=0, column=1, padx=5, pady=5)

frame3 = LabelFrame(mainframe, bg='#384048', padx=10, pady=10, relief=RAISED)
frame3.grid(row=1, column=0, padx=5, pady=5)

frame4 = LabelFrame(mainframe, bg='#384048', padx=10, pady=10, relief=RAISED)
frame4.grid(row=1, column=1, padx=5, pady=5)

#the widgets
pump = Button(frame4, padx=45, pady=40, bg='#708090', fg='#e8e8e8', command=pumpClick)
pump.grid(row=2, column=0)

fan = Button(frame4, padx=45, pady=40, bg='#708090', fg='#e8e8e8', command=fanClick)
fan.grid(row=2, column=1)

light = Button(frame4, padx=45, pady=40, bg='#708090', fg='#e8e8e8', command=lightClick)
light.grid(row=2, column=2)

ph1 = Button(frame4, padx=45, pady=40, bg='#708090', fg='#e8e8e8', command=ph1Click)
ph1.grid(row=5, column=0)
ph2 = Button(frame4, padx=45, pady=40, bg='#708090', fg='#e8e8e8', command=ph2Click)
ph2.grid(row=5, column=1)

resfil = Button(frame4, padx=45, pady=40, bg='#708090', fg='#e8e8e8', command=resfilClick)
resfil.grid(row=5, column=2)

#gauges
#water Management
canvas = Canvas(frame, width=50, height=200, bg='black', highlightbackground='black')
canvas.grid(row=2, column=1)
canvas.create_rectangle(50, 100, 1, 200, width=5, fill='blue')

canvas = Canvas(frame, width=50, height=200, bg='black', highlightbackground='black')
canvas.grid(row=2, column=3)
canvas.create_rectangle(50, 100, 1, 200, width=5, fill='blue')

canvas = Canvas(frame, width=50, height=200, bg='black', highlightbackground='black')
canvas.grid(row=2, column=5)
canvas.create_rectangle(50, 100, 1, 200, width=5, fill='blue')

canvas = Canvas(frame, width=50, height=200, bg='black', highlightbackground='black')
canvas.grid(row=2, column=7)
canvas.create_rectangle(50, 100, 1, 200, width=5, fill='blue')

#nutrient Management
canvas = Canvas(frame2, width=50, height=200, bg='black', highlightbackground='black')
canvas.grid(row=2, column=0)
canvas.create_rectangle(50, 100, 1, 200, width=5, fill='blue')

canvas = Canvas(frame2, width=50, height=200, bg='black', highlightbackground='black')
canvas.grid(row=2, column=1)
canvas.create_rectangle(50, 100, 1, 200, width=5, fill='blue')

canvas = Canvas(frame2, width=50, height=200, bg='black', highlightbackground='black')
canvas.grid(row=2, column=2)
canvas.create_rectangle(50, 100, 1, 200, width=5, fill='blue')

#Environment Management
canvas = Canvas(frame3, width=50, height=200, bg='black', highlightbackground='black')
canvas.grid(row=2, column=0)
canvas.create_rectangle(50, 100, 1, 200, width=5, fill='blue')

canvas = Canvas(frame3, width=50, height=200, bg='black', highlightbackground='black')
canvas.grid(row=2, column=1)
canvas.create_rectangle(50, 100, 1, 200, width=5, fill='blue')

canvas = Canvas(frame3, width=50, height=200, bg='black', highlightbackground='black')
canvas.grid(row=2, column=2)
canvas.create_rectangle(50, 100, 1, 200, width=5, fill='blue')


#Water Management labels
gauge0 = Label(frame, text="Water\nManagement\n\n", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge0.grid(row=0, column=4)
gauge1 = Label(frame, text="Water\nLevel", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge1.grid(row=1, column=1)
gauge2 = Label(frame, text="Pump\nFlow", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge2.grid(row=1, column=3)
gauge3 = Label(frame, text="Retn\nFlow", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge3.grid(row=1, column=5)
gauge4 = Label(frame, text="Fill\nFlow", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge4.grid(row=1, column=7)

#Nutrient Management
gauge5 = Label(frame2, text="Nutrient\nManagement\n\n", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge5.grid(row=0, column=1)
gauge6 = Label(frame2, text="PH\nLevel", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge6.grid(row=1, column=0)
gauge7 = Label(frame2, text="PH UP\nFlow", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge7.grid(row=1, column=1)
gauge8 = Label(frame2, text="PH DWN\nFlow", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge8.grid(row=1, column=2)
#gauge9 = Label(frame2, text="\nLevel", font="none 12 bold", bg='#384048', fg='#e8e8e8')
#gauge9.grid(row=1, column=3)

#Environment Management
gauge9 = Label(frame3, text="Environment\nManagement\n\n", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge9.grid(row=0, column=1)
gauge10 = Label(frame3, text="Temp", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge10.grid(row=1, column=0)
gauge11 = Label(frame3, text="Humidity", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge11.grid(row=1, column=1)
gauge12 = Label(frame3, text="PH\nLevel", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge12.grid(row=1, column=2)
#gauge7 = Label()

#Widget Labels
label0 = Label(frame4, text="System\nManual Over-Ride\n", font="none 12 bold", bg='#384048', fg='#e8e8e8')
label0.grid(row=0, column=1)
label1 = Label(frame4, text="Pump", bg='#384048', fg='#e8e8e8')
label1.grid(row=1, column=0)
label2 = Label(frame4, text="Fan", bg='#384048', fg='#e8e8e8')
label2.grid(row=1, column=1)
label3 = Label(frame4, text="Light", bg='#384048', fg='#e8e8e8')
label3.grid(row=1, column=2)
label4 = Label(frame4, text="\nPH UP", bg='#384048', fg='#e8e8e8')
label4.grid(row=4, column=0)
label5 = Label(frame4, text="\nPH Down", bg='#384048', fg='#e8e8e8')
label5.grid(row=4, column=1)
label6 = Label(frame4, text="\nReservoir Fill", bg='#384048', fg='#e8e8e8')
label6.grid(row=4, column=2)
#label1 = Label(root, text="")

#WM Slider
#Create a scale widget
scale = Scale(frame, orient=VERTICAL, from_=100,
                         to=0, length=200, width=10, sliderlength=15, bg='#384048',
                            showvalue=True)
scale.grid(row=2, column=2)

scale = Scale(frame, orient=VERTICAL, from_=100,
                         to=0, length=200, width=10, sliderlength=15, bg='#384048',
                            showvalue=True)
scale.grid(row=2, column=4)

scale = Scale(frame, orient=VERTICAL, from_=100,
                         to=0, length=200, width=10, sliderlength=15, bg='#384048',
                            showvalue=True)
scale.grid(row=2, column=6)

root.mainloop()
