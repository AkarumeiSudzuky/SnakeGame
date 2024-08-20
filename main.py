from turtle import Turtle, Screen
import time
from Snake import Snake
from food import Food
from scoreboard import Scoreboard
from superFood import SuperFood
import random

# Screen settings
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

# Objects
snake = Snake()
food = Food()
superFood = SuperFood(screen)
scoreboard = Scoreboard()

# Snake manipulation
game_on = True
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# The game
while game_on:  # if snake consists of 3 blocks 3->2, 2->1 and 1 is moving into direction
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision of snake and food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_points()
        snake.extend_snake()

    # Detect collision with a wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        superFood.stop_blinking()

        # Detect collision with the tail
    for snake_part in snake.segments[1:]:
        if snake.head.distance(snake_part) < 5:
            scoreboard.reset()
            snake.reset()
            superFood.stop_blinking()

    # Detect collision of snake and superFood
    if superFood.isvisible() and snake.head.distance(superFood) < 15:
        for _ in range(3):
            scoreboard.add_points()
            snake.extend_snake()
        superFood.stop_blinking()  # Stop blinking and hide






screen.exitonclick()



