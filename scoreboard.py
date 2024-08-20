from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as file:
            self.highest_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 270)
        self.print_score()


    def print_score(self):
        self.clear()
        self.write(f"Score {self.score} / Highest score {self.highest_score}", align='center', font=('Arial', 18, 'bold'))

    def add_points(self):
        self.score += 1
        self.print_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=('Arial', 24, 'bold'))

    def reset(self):
        self.clear()
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("score.txt", "w") as file:
                file.write(str(self.score))
        self.score =0
        self.print_score()

    def write_score(self):
        file = open("score.txt", "w")
        file.write(self.score)
        file.close()