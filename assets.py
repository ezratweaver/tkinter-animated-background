from tkinter import PhotoImage, Tk
from os import path, chdir
from sys import argv

EXE_DIR = path.dirname(argv[0])
chdir(EXE_DIR)

WINDOW_COLOR = "#3556FB"
window = Tk()

class Assets():
    image_circle1 = PhotoImage(file="Assets/circle1.png")