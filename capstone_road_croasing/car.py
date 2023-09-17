from turtle import Turtle
import random

CAR_COLOR = ['red', 'green', 'blue', 'yellow', 'black', 'orange', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_Y_POSITION = [150, 100, 50, 0, -50, -100, -150]


class Car():
	def __init__(self):
		self.y = 0
		self.all_cars = []
		self.car_speed = MOVE_INCREMENT

	def car_create(self):
		create_a_new_car = random.randint(1, 6)
		if create_a_new_car == 1:
			new_car = Turtle('square')
			new_car.shape('square')
			new_car.shapesize(stretch_wid=1, stretch_len=2)
			new_car.penup()
			new_car.color(random.choice(CAR_COLOR))
			y_coordinate = random.randint(-240, 240)
			new_car.goto(-400, y_coordinate)
			self.all_cars.append(new_car)

	def car_moving(self):
		for car in self.all_cars:
			car.forward(self.car_speed)

	def level_up(self):
		self.car_speed += MOVE_INCREMENT
