from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.color("Blue")
        self.penup()
        self.food_spawn()

    def food_spawn(self):
        self.goto(random.randint(-270, 270), random.randint(-270, 270))
