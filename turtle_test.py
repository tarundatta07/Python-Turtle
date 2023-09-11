from turtle import Turtle, Screen
import turtle as turtle_module
from random import choice, randint
import colorgram

turtle = Turtle()
# turtle.color("coral")

# for t in range(4):
#     turtle.forward(100)
#     turtle.left(90)
# print(turtle)
#
# pen = Turtle()
# for _ in range(15):
#     # Set the initial position of the turtle for a new line
#     pen.penup()
#     pen.goto(-200, 0)
#     pen.pendown()
#
turtle_color = [
    "green yellow",
    "medium sea green",
    "dark turquoise",
    "black",
    "deep sky blue",
    "deep pink",
    "dark slate blue",
    "red",
    "gold",
    "medium spring green",
    "blue violet",
    "light sky blue",
    "saddle brown",
    "indigo",
    "black",
]

#
# # DRAWING DIFFERENT SHAPE
# def draw_shape(num_of_side):
#     angel = 360 / num_of_side
#     for shape in range(num_of_side):
#         turtle.forward(200)
#         turtle.right(angel)
#
#
# for side in range(3, 10):
#     turtle.color(choice(turtle_color))
#     draw_shape(side)
#
# # DRAWING RANDOM WALK
# direction = [0, 90, 180, 270]
# turtle.pensize(5)
# turtle.speed("fastest")
# for iteration in range(100):
#     turtle.dot(20)
#     turtle.color(choice(turtle_color))
#     turtle.forward(30)
#     turtle.setheading(choice(direction))

# DRAWING SPIRAL GRAPH
# turtle.speed("fastest")
# for count in range(100):
#     turtle.circle(150)
#     turtle.color(choice(turtle_color))
#     current_heading = turtle.heading()
#     turtle.setheading(current_heading + 5)

# rgb_color_list = []
# colors = colorgram.extract('hirst.jpeg', 20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color = (r, g, b)
#     rgb_color_list.append(rgb_color)
# print(rgb_color_list)

color_list = [(235, 232, 227), (230, 233, 239), (239, 231, 235), (227, 236, 230), (198, 162, 101), (63, 90, 126), (139, 170, 191), (136, 91, 50), (132, 28, 53), (219, 205, 120), (29, 40, 65), (78, 16, 35), (149, 62, 85), (162, 155, 53), (184, 141, 158), (132, 182, 145), (48, 56, 99), (180, 97, 107), (56, 35, 22), (68, 130, 106)]
turtle_module.colormode(255)
# turtle = turtle_module.Turtle()
turtle.penup()
turtle.hideturtle()
turtle.speed("fastest")
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
num_of_row = 100
count = 0

for dot in range(1, num_of_row + 1):
    turtle.dot(20, choice(color_list))
    turtle.forward(50)
    if dot % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)
        count += 1

print(count)
my_screen = Screen()
print(my_screen.canvwidth)
my_screen.exitonclick()
