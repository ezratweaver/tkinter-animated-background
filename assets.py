from tkinter import PhotoImage, Tk
from os import path, chdir
from sys import argv
from itertools import chain

EXE_DIR = path.dirname(argv[0])
chdir(EXE_DIR)

WINDOW_COLOR = "#3556FB"
window = Tk()

class Assets():
    image_circle = PhotoImage(file="Assets/circle.png")
    image_square = PhotoImage(file="Assets/square.png")
    image_star = PhotoImage(file="Assets/star.png")
    image_triangle = PhotoImage(file="Assets/triangle.png")


asset_manifest = [getattr(Assets, x) for x in dir(Assets) if x.startswith("image")]
asset_manifest = list(chain(asset_manifest * 7))