from turtle import Screen
import time
import random

from capstone_road_croasing.car import Car
from capstone_road_croasing.player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.title('Capstone Road Crossing')
screen.tracer(0)
screen.listen()

car = Car()
scoreboard = Scoreboard()
player = Player()
player.shape('turtle')

screen.onkey(player.move_up, 'Up')
screen.onkey(player.move_down, 'Down')

game_is_on = True
while game_is_on:

	time.sleep(0.1)
	screen.update()
	car.car_create()
	car.car_moving()

	for car_move in car.all_cars:
		if car_move.distance(player) < 20:
			scoreboard.game_over()
			game_is_on = False
			print("Game Over")
			# player.goto_start_position()

	if player.cross_finish_line():
		car.level_up()
		scoreboard.increase_level()
		player.goto_start_position()

screen.exitonclick()
