from tkinter import Tk, Canvas
from assets import Assets


WINDOW_COLOR = "#3556FB"
window = Tk()


class Background:

    def __init__(self):
        background = Canvas(window, bg=WINDOW_COLOR,
                            height=500, width = 800,
                            bd=0, highlightthickness=0,
                            relief="ridge")
        background.pack()

window.geometry("800x500")
window.configure(bg=WINDOW_COLOR)
window.title("Tkinter Math Flash Cards")
window.resizable(False, False)
window.mainloop()