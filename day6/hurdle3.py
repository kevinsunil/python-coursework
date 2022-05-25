# http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def movement():
    i = 0
    turn_left()
    while wall_on_right():
        move()
        i +=  1
    if right_is_clear():
        turn_right()
        move()
        turn_right()
    for k in range(i):
        move()
    turn_left()
while not at_goal():
    if wall_in_front():
        movement()
    else:
        move()
