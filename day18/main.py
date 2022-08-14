from turtle import Turtle, Screen
import random
import colorgram

test_turtle = Turtle()
test_turtle.color("Blue")
colors = ["royal blue", "silver", "red", "dark goldenrod", "green", "cyan", "teal", "light pink"]
direction = [0, 90, 180, 270]
screen = Screen()  # used for controlling the turtle screen
screen.colormode(255)
new_colors = colorgram.extract('537b6eca8c43b46982da4c2af786fb1124592d0a-1200x995.jpg', 10)


def hirst_painting():
    test_turtle.penup()
    test_turtle.setposition(-225, -225)
    for _ in range(10):
        xcor = test_turtle.xcor()
        ycor = test_turtle.ycor()
        for i in range(10):
            # test_turtle.penup()
            # test_turtle.fd(20)
            test_turtle.pendown()
            spot_color = random.choice(new_colors)
            test_turtle.pencolor(spot_color.rgb)
            test_turtle.dot(20)
            test_turtle.penup()
            test_turtle.fd(50)
        test_turtle.setx(xcor)
        test_turtle.sety(ycor + 50)
    test_turtle.hideturtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    test_turtle.pencolor(r, g, b)


def square():
    for i in range(0, 4):
        test_turtle.fd(100)
        test_turtle.lt(90)


def dashed_line():
    for _ in range(20):
        test_turtle.fd(5)
        test_turtle.penup()
        test_turtle.fd(5)
        test_turtle.pendown()


def weird_shapes():
    for i in range(3, 11):
        angle = 360 / i
        test_turtle.color(random.choice(colors))
        for _ in range(i):
            test_turtle.fd(100)
            test_turtle.lt(angle)


def random_walk():
    test_turtle.pensize(8)
    for _ in range(100):
        # test_turtle.color(random.choice(colors))
        random_color()
        test_turtle.setheading(random.choice(direction))
        test_turtle.fd(30)


def spirograph():
    test_turtle.speed(0)
    for i in range(36):
        # random_color()
        # test_turtle.left(i)
        test_turtle.circle(100)
        current_angle = test_turtle.heading()
        test_turtle.setheading(current_angle + 10)


# dashed_line()
# weird_shapes()
# random_walk()
# spirograph()
hirst_painting()
# square()

screen.exitonclick()
