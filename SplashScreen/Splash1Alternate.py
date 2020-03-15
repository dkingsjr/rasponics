"""
Python Tkinter Splash Screen

This script holds the class SplashScreen, which is simply a window without
the top bar/borders of a normal window.

The window width/height can be a factor based on the total screen dimensions
or it can be actual dimensions in pixels. (Just edit the useFactor property)

Very simple to set up, just create an instance of SplashScreen, and use it as
the parent to other widgets inside it.

www.sunjay-varma.com
"""

from tkinter import *

class SplashScreen(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack(side=TOP, fill=BOTH, expand=YES)

        # get screen width and height
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        #w = (useFactor and  ws*width) or width
        #h = (useFactor and ws*height) or height
        # calculate position x, y
        #x = (ws/2) - (w/2) 
        #y = (hs/2) - (h/2)
        self.master.geometry(("%dx%d")%(ws,hs))
        #self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        
        self.master.overrideredirect(True)
        self.lift()

if __name__ == '__main__':
    root = Tk()

    sp = SplashScreen(root)
    sp.config(bg="#bc1142")

    m = Label(sp, text="RasPonics Hydroponics Farm\n\nFeeding the world, one farm at a time.")
    m.pack(side=TOP, expand=YES)
    m.config(bg="#bc1142", fg="white", justify=CENTER, font=("calibri", 29,))
    
    Button(sp, text="Press this button to kill the program", bg='#75a927', fg="white", command=root.destroy).pack(side=BOTTOM)
    root.mainloop()