from tkinter import PhotoImage, Tk
from os import path, chdir
from sys import argv

EXE_DIR = path.dirname(argv[0])
chdir(EXE_DIR)

WINDOW_COLOR = "#3556FB"
window = Tk()

class Assets():
    image_circle1 = PhotoImage(file="Assets/circle1.png")
    image_circle2 = PhotoImage(file="Assets/circle2.png")
    image_circle3 = PhotoImage(file="Assets/circle3.png")
    image_circle4 = PhotoImage(file="Assets/circle4.png")
    image_square1 = PhotoImage(file="Assets/square1.png")
    image_square2 = PhotoImage(file="Assets/square2.png")
    image_square3 = PhotoImage(file="Assets/square3.png")
    image_star1 = PhotoImage(file="Assets/star1.png")
    image_star2 = PhotoImage(file="Assets/star2.png")
    image_star3 = PhotoImage(file="Assets/star3.png")
    image_triangle1 = PhotoImage(file="Assets/triangle1.png")


asset_manifest = [getattr(Assets, x) for x in dir(Assets) if x.startswith("image")]
