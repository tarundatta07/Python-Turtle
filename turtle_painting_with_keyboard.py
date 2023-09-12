from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
screen.listen()


def move_forward():
    # turtle.dot(10)
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def turn_left():
    new_heading = turtle.heading() + 10
    turtle.setheading(new_heading)


def turn_right():
    new_heading = turtle.heading() - 10
    turtle.setheading(new_heading)


def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.onkey(move_forward, "d")
screen.onkey(move_backward, "a")
screen.onkey(turn_left, "w")
screen.onkey(turn_right, "x")
screen.onkey(clear, "c")

screen.exitonclick()
