from tkinter import *
import RPi.GPIO as GPIO

from PIL import ImageTk, Image
#import os


#==============================Button Functionality==============
pwm = None

GPIO5 = 5
GPIO7 = 7
GPIO8 = 8
GPIO10 = 10
GPIO11 = 11
GPIO12 = 12
GPIO15 = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO5, GPIO.OUT)
GPIO.setup(GPIO7, GPIO.OUT)
GPIO.setup(GPIO8, GPIO.OUT)
GPIO.setup(GPIO10, GPIO.OUT)
GPIO.setup(GPIO11, GPIO.OUT)
GPIO.setup(GPIO12, GPIO.OUT)
GPIO.setup(GPIO15, GPIO.OUT)

GPIO5_state = True
GPIO7_state = True
GPIO8_state = True
GPIO10_state = True
GPIO11_state = True
GPIO12_state = True
GPIO15_state = True

def pump():
    global GPIO5_state
    if GPIO5_state == True:
        GPIO.output(GPIO5, GPIO5_state)
        GPIO5_state = False
        ONlabel = Label(frame4, text="ON", font="none 12", bg='#384048', fg="green")
        ONlabel.grid(row=1, column=0)
    else:
        GPIO.output(GPIO5, GPIO5_state)
        GPIO5_state = True
        ONlabel = Label(frame4, text="OFF", font="none 12", bg='#384048',  fg="red")
        ONlabel.grid(row=1, column=0)


def fan():
    global GPIO7_state
    if GPIO7_state == True:
        GPIO.output(GPIO7, GPIO7_state)
        GPIO7_state = False
        OFFlabel = Label(frame4, text="ON", font="none 12", bg='#384048', fg="green")
        OFFlabel.grid(row=1, column=1)
    else:
        GPIO.output(GPIO7, GPIO7_state)
        GPIO7_state = True
        OFFlabel = Label(frame4, text="OFF", font="none 12", bg='#384048', fg="red")
        OFFlabel.grid(row=1, column=1)


def light():
    global GPIO8_state
    if GPIO8_state == True:
        GPIO.output(GPIO8, GPIO8_state)
        GPIO8_state = False
        OFFlabel = Label(frame4, text="ON", font="none 12",  bg='#384048', fg="green")
        OFFlabel.grid(row=1, column=2)
    else:
        GPIO.output(GPIO8, GPIO8_state)
        GPIO8_state = True
        OFFlabel = Label(frame4, text="OFF", font="none 12", bg='#384048', fg="red")
        OFFlabel.grid(row=1, column=2)


def heat():
    global GPIO10_state
    if GPIO10_state == True:
        GPIO.output(GPIO10, GPIO10_state)
        GPIO10_state = False
        OFFlabel = Label(frame4, text="ON", font="none 12",  bg='#384048', fg="green")
        OFFlabel.grid(row=1, column=3)
    else:
        GPIO.output(GPIO10, GPIO10_state)
        GPIO10_state = True
        OFFlabel = Label(frame4, text="OFF", font="none 12", bg='#384048', fg="red")
        OFFlabel.grid(row=1, column=3)
        
def ph1():
    global GPIO11_state
    if GPIO11_state == True:
        GPIO.output(GPIO11, GPIO11_state)
        GPIO11_state = False
        ONlabel = Label(frame4, text="ON", font="none 12", bg='#384048', fg="green")
        ONlabel.grid(row=1, column=4)
    else:
        GPIO.output(GPIO11, GPIO11_state)
        GPIO11_state = True
        ONlabel = Label(frame4, text="OFF", font="none 12", bg='#384048', fg="red")
        ONlabel.grid(row=1, column=4)


def ph2():
    global GPIO12_state
    if GPIO12_state == True:
        GPIO.output(GPIO12, GPIO12_state)
        GPIO12_state = False
        OFFlabel = Label(frame4, text="ON", font="none 12", bg='#384048', fg="green")
        OFFlabel.grid(row=1, column=5)
    else:
        GPIO.output(GPIO12, GPIO12_state)
        GPIO12_state = True
        OFFlabel = Label(frame4, text="OFF", font="none 12", bg='#384048', fg="red")
        OFFlabel.grid(row=1, column=5)


def resfil():
    global GPIO15_state
    if GPIO15_state == True:
        GPIO.output(GPIO15, GPIO15_state)
        GPIO15_state = False
        OFFlabel = Label(frame4, text="ON", font="none 12", bg='#384048', fg="green")
        OFFlabel.grid(row=1, column=6)
    else:
        GPIO.output(GPIO15, GPIO15_state)
        GPIO15_state = True
        OFFlabel = Label(frame4, text="OFF", font="none 12", bg='#384048', fg="red")
        OFFlabel.grid(row=1, column=6)


        
#============================================================================
#============================================================================

#path = home/pi/PycharmProjects/rasponics/PowerRPI.png
#=================================the window=================================
root = Tk()
root.title("RasPonics 1.0")
root.configure(bg='#384048')
#Removes frame from the window. Commented out for now due to development.
#root.overrideredirect(True)

#window dimensions(auto size)
RWidth=root.winfo_screenwidth()
RHeight=root.winfo_screenheight()
root.geometry(("%dx%d")%(RWidth,RHeight))

#img = ImageTK.PhotoImage(image.open(path))
#panel = tk.Label(mainframe, image = img)
#panel.pack(side = "bottom", fill = "both", expaand = "yes")

#=======================================Frames===============================
mainframe = LabelFrame(root, bg='#384048', padx=10, pady=10, relief=SUNKEN)
mainframe.pack(fill="both", expand=True, padx=10, pady=10)
mainframe.columnconfigure(0, weight=2)
mainframe.columnconfigure(1, weight=2)
mainframe.columnconfigure(2, weight=2)


frame = LabelFrame(mainframe, bg='#384048', padx=10, pady=10, relief=RAISED)
frame.grid(row=1, column=0, padx=5, pady=5)


frame2 = LabelFrame(mainframe, bg='#384048', padx=10, pady=10, relief=RAISED)
frame2.grid(row=1, column=1, padx=5, pady=5)

frame3 = LabelFrame(mainframe, bg='#384048', padx=10, pady=10, relief=RAISED)
frame3.grid(row=1, column=3, padx=5, pady=5)

frame4 = LabelFrame(mainframe, bg='#384048', padx=10, pady=10, relief=RAISED)
frame4.grid(row=3, column=1, padx=20, pady=20)

#==============================================================================
#==============================================================================

#===================================the widgets================================
pump = Button(frame4, padx=5, pady=5, text="Pump", font = "none 12 bold" , bg='#708090', fg='#e8e8e8', command=pump)
pump.grid(row=2, column=0, padx=5, pady=5)

fan = Button(frame4, padx=10, pady=5, text="Fan", font = "none 12 bold" , bg='#708090', fg='#e8e8e8', command=fan)
fan.grid(row=2, column=1, padx=5, pady=5)

light = Button(frame4, padx=5, pady=5, text="Light", font = "none 12 bold" , bg='#708090', fg='#e8e8e8', command=light)
light.grid(row=2, column=2,padx=5, pady=5)

heat = Button(frame4, padx=5, pady=5, text="Heater", font = "none 12 bold" , bg='#708090', fg='#e8e8e8', command=heat)
heat.grid(row=2, column=3,padx=5, pady=5)

ph1 = Button(frame4, padx=5, pady=5, text="PH\nUP", font = "none 12 bold" , bg='#708090', fg='#e8e8e8', command=ph1)
ph1.grid(row=2, column=4,padx=5, pady=5)

ph2 = Button(frame4, padx=5, pady=5, text="PH\nDown", font = "none 12 bold" , bg='#708090', fg='#e8e8e8', command=ph2)
ph2.grid(row=2, column=5,padx=5, pady=5)

resfil = Button(frame4, padx=5, pady=5, text="Res\nFill", font = "none 12 bold" , bg='#708090', fg='#e8e8e8', command=resfil)
resfil.grid(row=2, column=6,padx=5, pady=5)

exit = Button(mainframe, text="Terminate\nRasponics", font = "Helvetica 12 bold", bg='#708090', fg='#C51A4A', command=root.destroy)
exit.grid(row=4, column=1)

#===================================gauges=====================================
#water Management
canvas = Canvas(frame, width=50, height=200, bg='black', highlightbackground='black')
canvas.grid(row=2, column=1, padx=20)
canvas.create_rectangle(50, 100, 1, 200, width=5, fill='blue')

canvas = Canvas(frame, width=50, height=200, bg='black', highlightbackground='black')
canvas.grid(row=2, column=3,)
canvas.create_rectangle(50, 100, 1, 200, width=5, fill='blue')

canvas = Canvas(frame, width=50, height=200, bg='black', highlightbackground='black')
canvas.grid(row=2, column=5)
canvas.create_rectangle(50, 100, 1, 200, width=5, fill='blue')

canvas = Canvas(frame, width=50, height=200, bg='black', highlightbackground='black')
canvas.grid(row=2, column=7)
canvas.create_rectangle(50, 100, 1, 200, width=5, fill='blue')

canvas = Canvas(mainframe, width = 150, height = 50)  
canvas.grid(row=3, column=0)  
img = ImageTk.PhotoImage(Image.open("Power RPI.png"))
canvas.create_image(10, 10, anchor=W, image=img) 

#nutrient Management
canvas = Canvas(frame2, width=50, height=200, bg='black', highlightbackground='black')
canvas.grid(row=2, column=0, padx=10)
canvas.create_rectangle(50, 100, 1, 200, width=5, fill='blue')

canvas = Canvas(frame2, width=50, height=200, bg='black', highlightbackground='black')
canvas.grid(row=2, column=1, padx=10)
canvas.create_rectangle(50, 100, 1, 200, width=5, fill='blue')

canvas = Canvas(frame2, width=50, height=200, bg='black', highlightbackground='black')
canvas.grid(row=2, column=2, padx=10)
canvas.create_rectangle(50, 100, 1, 200, width=5, fill='blue')

#Environment Management
canvas = Canvas(frame3, width=50, height=200, bg='black', highlightbackground='black')
canvas.grid(row=2, column=0, padx=10)
canvas.create_rectangle(50, 100, 1, 200, width=5, fill='blue')

canvas = Canvas(frame3, width=50, height=200, bg='black', highlightbackground='black')
canvas.grid(row=2, column=1, padx=10)
canvas.create_rectangle(50, 100, 1, 200, width=5, fill='blue')

canvas = Canvas(frame3, width=50, height=200, bg='black', highlightbackground='black')
canvas.grid(row=2, column=2, padx=10)
canvas.create_rectangle(50, 100, 1, 200, width=5, fill='blue')

#================================Labels==================================
#Frame Labels
gauge0 = Label(mainframe, text="\n\nWater\nManagement", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge0.grid(row=0, column=0)

gauge5 = Label(mainframe, text="\n\nNutrient\nManagement", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge5.grid(row=0, column=1)

gauge9 = Label(mainframe, text="\n\nEnvironment\nManagement", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge9.grid(row=0, column=3)

label0 = Label(mainframe, text="\n\nSystem\nManual Over-Ride", font="none 12 bold", bg='#384048', fg='#e8e8e8')
label0.grid(row=2, column=1)

#Water Management labels
gauge1 = Label(frame, text="Water\nLevel", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge1.grid(row=1, column=1)
gauge2 = Label(frame, text="Pump\nFlow", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge2.grid(row=1, column=3)
gauge3 = Label(frame, text="Retn\nFlow", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge3.grid(row=1, column=5)
gauge4 = Label(frame, text="Fill\nFlow", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge4.grid(row=1, column=7)

#Nutrient Management
gauge6 = Label(frame2, text="PH\nLevel", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge6.grid(row=1, column=0)
gauge7 = Label(frame2, text="PH U\nFlow", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge7.grid(row=1, column=1)
gauge8 = Label(frame2, text="PH D\nFlow", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge8.grid(row=1, column=2)
#gauge9 = Label(frame2, text="\nLevel", font="none 12 bold", bg='#384048', fg='#e8e8e8')
#gauge9.grid(row=1, column=3)

#Environment Management
gauge10 = Label(frame3, text="Temp", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge10.grid(row=1, column=0)
gauge11 = Label(frame3, text="Humidity", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge11.grid(row=1, column=1)
gauge12 = Label(frame3, text="PH\nLevel", font="none 12 bold", bg='#384048', fg='#e8e8e8')
gauge12.grid(row=1, column=2)

#===========================WM Slider======================
#Create a scale widget
scale = Scale(frame, orient=VERTICAL, from_=100, to=0, length=200, width=10, sliderlength=15, bg='#384048', showvalue=True)
scale.grid(row=2, column=2, sticky=E)

scale = Scale(frame, orient=VERTICAL, from_=100, to=0, length=200, width=10, sliderlength=15, bg='#384048', showvalue=True)
scale.grid(row=2, column=4)

scale = Scale(frame, orient=VERTICAL, from_=100, to=0, length=200, width=10, sliderlength=15, bg='#384048', showvalue=True)
scale.grid(row=2, column=6)

#blank columns

root.mainloop()
GPIO.cleanup()
