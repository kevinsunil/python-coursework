from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.updatelevel()

    def updatelevel(self):
        self.clear()
        self.goto(-25, 250)
        self.write(f'Level: {self.level}', align='center', font=FONT)

    def levelup(self):
        self.level += 1
        self.updatelevel()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align='center', font=FONT)
