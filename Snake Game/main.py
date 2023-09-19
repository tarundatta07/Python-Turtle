from turtle import Screen
import time

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

food = Food()
snake = Snake()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
	screen.update()
	time.sleep(0.1)
	snake.move_snake()

	if snake.head.distance(food) < 15:
		food.regenerate_food()
		snake.extend_snake()
		scoreboard.increase_score()

	if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
		scoreboard.reset_score()
		snake.snake_reset()

	for segment in snake.combine_blocks[1:]:
		if snake.head.distance(segment) < 10:
			scoreboard.reset_score()
			snake.snake_reset()

screen.exitonclick()
