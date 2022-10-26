import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)
screen.title("Pong game")


def new_paddle(x, y):
    paddle = Turtle()
    paddle.shape("square")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.color("white")
    paddle.penup()
    paddle.goto(x, y)
    return paddle


paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
# paddle_moves = Paddle_move()
screen.update()

game_on = True


def check_move():
    screen.listen()
    screen.onkeypress(paddle_1.move_upwards, "Up")
    screen.onkeypress(paddle_1.move_downwards, "Down")
    screen.onkeypress(paddle_2.move_upwards, "w")
    screen.onkeypress(paddle_2.move_downwards, "s")


while game_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()
    check_move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_vertical()
    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.bounce_horizontal()
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()
screen.exitonclick()
