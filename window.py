from tkinter import Canvas
from assets import asset_manifest, window, WINDOW_COLOR
from random import randint, choice

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
                randint(0, 800),
                randint(0, 500),
                image=image))

RANDOM_VELOCITY = [-2, -1, 1, 2]
COLLISION_TOLERANCE = 40

class BackgroundObject:

    def __init__(self, id, object, start_x, end_x, start_y, end_y):
        self.id = id
        self.object = object
        self.x_velocity = choice(RANDOM_VELOCITY)
        self.y_velocity = choice(RANDOM_VELOCITY)
        self.start_x = start_x
        self.end_x = end_x
        self.start_y = start_y
        self.end_y = end_y
        self.cordinates = [0, 0]

    def start_animation(self):
        current_cordinates = bg.background.coords(self.object)

        if BackgroundObject.is_near(current_cordinates[0], self.start_x, 3):
            self.x_velocity = abs(self.x_velocity)
        if BackgroundObject.is_near(current_cordinates[0], self.end_x, 3):
            self.x_velocity = -abs(self.x_velocity)
        if BackgroundObject.is_near(current_cordinates[1], self.start_y, 3):
            self.y_velocity = abs(self.y_velocity)
        if BackgroundObject.is_near(current_cordinates[1], self.end_y, 3):
            self.y_velocity = -abs(self.y_velocity)

        for obj in moving_objects:
            if obj.id == self.id:
                continue
            if BackgroundObject.is_near(self.cordinates[0], 
                obj.cordinates[0], COLLISION_TOLERANCE
            ) and BackgroundObject.is_near(self.cordinates[1], 
                obj.cordinates[1], COLLISION_TOLERANCE):
                self.x_velocity = self.x_velocity * -1
                self.y_velocity = self.y_velocity * -1

        self.cordinates = [current_cordinates[0] + self.x_velocity, 
                    current_cordinates[1] + self.y_velocity]

        bg.background.coords(self.object, *self.cordinates)

        bg.background.after(20, self.start_animation)

    @staticmethod
    def is_near(number, target, tolerance):
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

bg = Background()

moving_objects = []
for x, placed_image in enumerate(bg.placed_images):
    moving_objects.append(BackgroundObject(x, placed_image, 0, 800, 0, 500))
for object in moving_objects:
    object.start_animation()

window.geometry("800x500")
window.title("Wallpaper")
window.resizable(False, False)
window.mainloop()