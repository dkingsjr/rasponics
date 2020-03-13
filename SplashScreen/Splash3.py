# create a splash screen, 80% of display screen size, centered,
# displaying a GIF image with needed info, disappearing after 5 seconds
import tkinter as tk
import os

# uncomment below when ready for time.sleep towards bottom
# import time

##############################
# For Converting GUI Media to Tkinter-compatible image objects: tkinter doesn't do well with images that aren't GIF/ICO
# https://effbot.org/tkinterbook/photoimage.htm
from PIL import Image, ImageTk

root = tk.Tk()

# show no frame
root.overrideredirect(True)

# root dimensions
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (width*0.8, height*0.8, width*0.1, height*0.1))

# sets current directory to location of file
my_directory = os.path.dirname(os.path.realpath(__file__))

# your program media
my_icon = 'RasDrop'
my_splash = 'RasponicsLOGO1'
# my_media_folder = 'media'

# Tray/Program Icon
# icon_image = Image.open(f'/{my_directory}/{my_media_folder}/{my_icon}.png')
# photo = ImageTk.PhotoImage(icon_image)
# root.iconphoto(False, photo)

# take a .jpg picture you like, add text with a program like PhotoFilter
# (free from http://www.photofiltre.com) and save as a .gif image file
image_file = Image.open(f'{my_splash}.png')
image = ImageTk.PhotoImage(image_file)
canvas = tk.Canvas(root, height=height*0.8, width=width*0.8, bg="brown")
canvas.create_image(width*0.8/2, height*0.8/2, image=image)
canvas.pack()

# show the splash screen for 5000 milliseconds then destroy
# root.after(5000, root.destroy)

# if 'root.after(5000, root.destroy)' doesn't work this will:
# time.sleep(5000)
# root.destroy()

root.mainloop()

# your console program can start here ...
print("How did you like my informative splash screen?")