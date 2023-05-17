from tkinter import Canvas
from assets import Assets, window, WINDOW_COLOR
from random import randint

class Background:

    def __init__(self):
        self.background = Canvas(window, bg=WINDOW_COLOR,
                            height=500, width = 800,
                            bd=0, highlightthickness=0,
                            relief="ridge")
        self.background.pack()

        self.circle1 = self.background.create_image(
            randint(1, 800),
            randint(1, 500),
            image=Assets.image_circle1
        )

        self.triangle1 = self.background.create_image(
            randint(1, 800),
            randint(1, 500),
            image=Assets.image_triangle1
        )

        self.square1 = self.background.create_image(
            randint(1, 800),
            randint(1, 500),
            image=Assets.image_square2
        )

    def move_object(self, object,
                    x_velocity, y_velocity,
                    start_x, end_x,
                    start_y, end_y):
        current_cordinates = self.background.coords(object)

        new_cords = [current_cordinates[0] + x_velocity, 
                    current_cordinates[1] + y_velocity]

        self.background.coords(object, *new_cords)


        if current_cordinates[0] < start_x:
            x_velocity = abs(x_velocity)
        if current_cordinates[0] > end_x:
            x_velocity = -abs(x_velocity)
        if current_cordinates[1] < start_y:
            y_velocity = abs(y_velocity)
        if current_cordinates[1] > end_y:
            y_velocity = -abs(y_velocity)


        self.background.after(20, self.move_object,
                                        object, x_velocity, 
                                        y_velocity, start_x, end_x,
                                        start_y, end_y)


move_object_args = [3, 3, 50, 750, 50, 445]
bg = Background()
bg.move_object(bg.circle1, *move_object_args)
bg.move_object(bg.triangle1, *move_object_args)
bg.move_object(bg.square1, *move_object_args)

window.geometry("800x500")
window.title("Wallpaper")
window.resizable(False, False)
window.mainloop()