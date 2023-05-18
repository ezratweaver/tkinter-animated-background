from tkinter import Canvas
from assets import asset_manifest, window, WINDOW_COLOR
from random import randint

class Background:

    def __init__(self):
        self.background = Canvas(window, bg=WINDOW_COLOR,
                            height=500, width = 800,
                            bd=0, highlightthickness=0,
                            relief="ridge")
        self.background.pack()

        self.placed_images = []
        for image in asset_manifest:
            self.placed_images.append(self.background.create_image(
                randint(1, 800),
                randint(1, 500),
                image=image
            ))

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
    
    @staticmethod
    def is_near(self, number, target, tolerance):
        """
        Checks if a number is near another number within a given tolerance.
        
        Args:
            self: The class object
            number (float): The number to be checked.
            target (float): The target number.
            tolerance (float): The allowable difference between the numbers.
            
        Returns:
            bool: True if the number is near the target within the tolerance
        """
        return abs(number - target) <= tolerance


move_object_args = [3, 3, 0, 800, 0, 500]
bg = Background()

for placed_image in bg.placed_images:
    bg.move_object(placed_image, *move_object_args)

window.geometry("800x500")
window.title("Wallpaper")
window.resizable(False, False)
window.mainloop()