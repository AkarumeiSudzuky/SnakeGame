from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[len(self.segments)-1]

    def create_snake(self):
        for i in range(3):
            self.add_segment(STARTING_POSITIONS[i])

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def add_segment(self, pos):
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        segment.goto(pos)
        self.segments.append(segment)

    def extend_snake(self):
        self.add_segment(self.tail.position())

    def reset(self):
        # hiding dead snake
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        # Recreate the snake in the starting position
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[len(self.segments)-1]