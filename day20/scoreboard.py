from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"SCORE:{self.score} ", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER ", False, align=ALIGNMENT, font=FONT)
