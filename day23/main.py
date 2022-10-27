import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car = CarManager()
screen.update()


def check_move():
    screen.listen()
    screen.onkeypress(player.move_forwards, "Up")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    car.create_car()
    car.car_move()
    check_move()
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.check_levelup():
        scoreboard.levelup()
        car.levelup()

screen.exitonclick()
