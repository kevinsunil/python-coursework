from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def move_upwards(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)
        # paddle_1.settiltangle(90)
        # paddle_1.setheading(90)
        # paddle_1.fd(20)
        # screen.update()

    def move_downwards(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)
        # paddle_1.settiltangle(270)
        # paddle_1.setheading(270)
        # paddle_1.fd(20)
        # screen.update()
