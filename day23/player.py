from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
START_SPEED = 0.1


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.start_pos()

    def start_pos(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_forwards(self):
        y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y)

    def check_levelup(self):
        if self.ycor() > FINISH_LINE_Y:
            self.start_pos()
            return True
