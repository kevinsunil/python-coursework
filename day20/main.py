from turtle import Screen
import time
from snake_move import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.update()


def check_move():
    screen.listen()
    screen.onkey(snake.move_upwards, "Up")
    screen.onkey(snake.move_downwards, "Down")
    screen.onkey(snake.move_left, "Left")
    screen.onkey(snake.move_right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    check_move()
    snake.move()
    if snake.check_end():
        scoreboard.reset_score()
        snake.reset_snake()
        # game_on = False
        # scoreboard.game_over()
    if snake.head.distance(food) < 15:
        food.food_spawn()
        snake.extend()
        scoreboard.update_score()

screen.exitonclick()

