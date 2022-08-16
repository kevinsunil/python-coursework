from turtle import Turtle, Screen
import random

screen = Screen()
test_turtle = Turtle()
race_turtle = Turtle(shape="turtle")
race_turtle_2 = Turtle(shape="turtle")
race_turtle_3 = Turtle(shape="turtle")
race_turtle_4 = Turtle(shape="turtle")
race_turtle_5 = Turtle(shape="turtle")


def turtle_setup():
    race_turtle.penup()
    race_turtle.color("Red")
    race_turtle.goto(-230, -100)
    race_turtle_2.penup()
    race_turtle_2.color("Green")
    race_turtle_2.goto(-230, -50)
    race_turtle_3.penup()
    race_turtle_3.color("Blue")
    race_turtle_3.goto(-230, 0)
    race_turtle_4.penup()
    race_turtle_4.color("Yellow")
    race_turtle_4.goto(-230, 50)
    race_turtle_5.penup()
    race_turtle_5.color("Pink")
    race_turtle_5.goto(-230, 100)


def turtle_move():
    race_turtle.fd(random.randint(10, 50))
    race_turtle_2.fd(random.randint(10, 50))
    race_turtle_3.fd(random.randint(10, 50))
    race_turtle_4.fd(random.randint(10, 50))
    race_turtle_5.fd(random.randint(10, 50))


def turtle_check_end():
    if race_turtle.xcor() >= 210:
        return False
    elif race_turtle_2.xcor() >= 210:
        return False
    elif race_turtle_3.xcor() >= 210:
        return False
    elif race_turtle_4.xcor() >= 210:
        return False
    elif race_turtle_5.xcor() >= 210:
        return False
    else:
        return True


def check_race_winner():
    if race_turtle.xcor() >= 210:
        return "red"
    elif race_turtle_2.xcor() >= 210:
        return "green"
    elif race_turtle_3.xcor() >= 210:
        return "blue"
    elif race_turtle_4.xcor() >= 210:
        return "yellow"
    elif race_turtle_5.xcor() >= 210:
        return "pink"


def turtle_race():
    screen.setup(width=500, height=400)
    user_input = screen.textinput(title="Place your bet", prompt="Who's going to win? Enter a color: ")
    turtle_setup()
    race_on = True
    while race_on:
        turtle_move()
        check = turtle_check_end()
        if not check:
            race_on = False
    winner = check_race_winner()
    if user_input.lower() == winner:
        print("You won !!!! Congrats")
    else:
        print(f"Your bet was {user_input.lower()} but the winner was {winner}.... You Lose!!!")


def forwards():
    test_turtle.fd(20)


def backwards():
    test_turtle.bk(20)


def clockwise_turn():
    new_angle = test_turtle.heading() + 10
    test_turtle.setheading(new_angle)


def anti_clockwise_turn():
    new_angle = test_turtle.heading() - 10
    test_turtle.setheading(new_angle)


def clear():
    screen.resetscreen()


turtle_race()
# screen.listen()
# screen.onkeypress(forwards, "w")
# screen.onkeypress(backwards, "s")
# screen.onkeypress(clockwise_turn, "a")
# screen.onkeypress(anti_clockwise_turn, "d")
# screen.onkey(clear, "space")
screen.exitonclick()
