from tkinter import Canvas, Label
from assets import Assets, window, WINDOW_COLOR

class Background:

    def __init__(self):
        self.background = Canvas(window, bg=WINDOW_COLOR,
                            height=500, width = 800,
                            bd=0, highlightthickness=0,
                            relief="ridge")
        self.background.pack()

        self.circle1 = self.background.create_image(
            100,
            100,
            image=Assets.image_circle1
        )

        print(self.background.coords(self.circle1))

    def move_circle1(self):
        current_cordinates = self.background.coords(self.circle1)

        new_cords = [current_cordinates[0] + 3, current_cordinates[1]]

        self.background.coords(self.circle1, *new_cords)

        self.background.after(10, self.move_circle1)

bg = Background()
bg.move_circle1()

window.geometry("800x500")
window.configure(bg=WINDOW_COLOR)
window.title("Tkinter Math Flash Cards")
window.resizable(False, False)
window.mainloop()