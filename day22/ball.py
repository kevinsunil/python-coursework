from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce_vertical(self):
        self.ymove *= -1

    def bounce_horizontal(self):
        self.xmove *= -1
        self.ball_speed *= 0.8

    def reset(self):
        self.setposition(0, 0)
        self.ball_speed = 0.1
        self.bounce_horizontal()
