from turtle import Screen
import time

from pong_game.ball import Ball
from pong_game.scoreboard import Scoreboard
from pong_game.turtlepaddle import TurtlePaddle

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('PONG GAME')

screen.tracer(0)
left_paddle = TurtlePaddle((-350, 0), 'white')
right_paddle = TurtlePaddle((350, 0), 'blue')
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.move_up, 'Left')
screen.onkey(left_paddle.move_down, 'Right')
screen.onkey(right_paddle.move_up, 'Up')
screen.onkey(right_paddle.move_down, 'Down')

game_is_on = True

while game_is_on:
    time.sleep(ball.move_ball_speed)
    screen.update()
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.toggle_ball_y_direction()

    if ball.distance(right_paddle.paddle) < 50 and ball.xcor() > 320 or   ball.distance(left_paddle.paddle) < 50 and ball.xcor() < -320:
        ball.toggle_ball_x_direction()

    if ball.xcor() > 380 :
        ball.reset_ball()
        scoreboard.left_paddle_scoreboard()

    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.right_paddle_scoreboard()

screen.exitonclick()

