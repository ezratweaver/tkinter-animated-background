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
            179,
            226,
            image=Assets.image_circle1
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
            x_velocity = 3
        if current_cordinates[0] > end_x:
            x_velocity = -3


        self.background.after(30, self.move_object,
                                        object, x_velocity, 
                                        y_velocity, start_x, end_x,
                                        start_y, end_y)



bg = Background()
bg.move_object(bg.circle1, 3, 0, 50, 750, 0, 0)

window.geometry("800x500")
window.configure(bg=WINDOW_COLOR)
window.title("Tkinter Math Flash Cards")
window.resizable(False, False)
window.mainloop()