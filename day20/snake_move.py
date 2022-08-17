from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.all_snakes = []
        self.create_snake()
        self.head = self.all_snakes[0]

    def create_snake(self):
        for i in STARTING_POSITION:
            self.add_body(i)

    def move(self):
        for snake in range(len(self.all_snakes) - 1, 0, -1):
            xcor = self.all_snakes[snake - 1].xcor()
            ycor = self.all_snakes[snake - 1].ycor()
            self.all_snakes[snake].goto(xcor, ycor)
        self.all_snakes[0].fd(10)

    def move_upwards(self):
        if self.all_snakes[0].heading() != 270:
            self.all_snakes[0].setheading(90)

    def move_downwards(self):
        if self.all_snakes[0].heading() != 90:
            self.all_snakes[0].setheading(270)

    def move_left(self):
        if self.all_snakes[0].heading() != 0:
            self.all_snakes[0].setheading(180)

    def move_right(self):
        if self.all_snakes[0].heading() != 180:
            self.all_snakes[0].setheading(0)

    def add_body(self, position):
        snake = Turtle("square")
        snake.speed(0)
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.all_snakes.append(snake)

    def extend(self):
        self.add_body(self.all_snakes[-1].position())

    def check_end(self):
        snake = self.all_snakes[0]
        if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
            return True
        for new_snake in self.all_snakes[1:]:
            if self.head.distance(new_snake) < 5:
                return True
        return False
