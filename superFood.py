from food import Food
import random

class SuperFood(Food):
    def __init__(self, screen):
        super(SuperFood, self).__init__()
        self.screen = screen
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.hideturtle()
        self.time_left = 0
        self.blinking = False
        self.appear = random.randint(5000, 10000)
        self.show()

    def show(self):
        self.screen.ontimer(self.countdown, self.appear)

    def countdown(self):
        self.time_left = 15 # Total time for blinking
        self.refresh()
        self.blinking = True
        self._toggle_visibility()

    def _toggle_visibility(self):
        if self.time_left > 0 and self.blinking:
            if self.isvisible():
                self.hideturtle()
            else:
                self.showturtle()

            self.time_left -= 1
            # Toggle visibility every 500 ms (0.5 seconds)
            self.screen.ontimer(self._toggle_visibility, 300)
        else:
            self.hideturtle()
            self.blinking = False

    def stop_blinking(self):
        self.blinking = False
        self.hideturtle()
        self.appear = random.randint(5000, 10000)
        self.show()
