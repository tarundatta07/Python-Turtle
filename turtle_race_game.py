from turtle import Turtle, Screen
from random import random, randint


screen = Screen()
screen.setup(width=600, height=600)
game_is_on = False
select_turtle = screen.textinput(title="Make You Bet", prompt="Which Turtle You Want to Bet?")
if select_turtle:
    game_is_on = True
turtle_color = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'black']
turtle_y_position = [150, 100, 50, 0, -50, -100, -150]
all_turtle = []
for index in range(7):
    turtle = Turtle(shape="turtle")
    turtle.color(turtle_color[index])
    turtle.penup()
    turtle.goto(x=-280, y= turtle_y_position[index])
    all_turtle.append(turtle)

while game_is_on:

    for turtle in all_turtle:
        if turtle.xcor() > 270:
            wining_turtle = turtle.pencolor()
            if select_turtle == wining_turtle:
                print(f"Congratulation You Win The Race. The Wining Tutle is {wining_turtle.upper()}")
            else:
                print(f"You Lost The Race. The Wining Turtle is {wining_turtle.upper()}")
            game_is_on = False
        distance = randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
