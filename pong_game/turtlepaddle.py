from turtle import Turtle

MOVE_PADDLE = 20


class TurtlePaddle:

    def __init__(self, position, color):
        self.paddle = Turtle()
        self.paddle.color(color)
        self.paddle.penup()
        self.paddle.shape('square')
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.goto(position)

    def move_up(self):
        new_coordinate = self.paddle.ycor() + MOVE_PADDLE
        self.paddle.goto(self.paddle.xcor(), new_coordinate)

    def move_down(self):
        new_coordinate = self.paddle.ycor() - MOVE_PADDLE
        self.paddle.goto(self.paddle.xcor(), new_coordinate)
