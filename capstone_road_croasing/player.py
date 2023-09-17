from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280


class Player(Turtle):
	def __init__(self):
		super().__init__()
		self.penup()
		self.color('blue')
		self.setheading(90)
		self.goto_start_position()
		self.forward(MOVE_DISTANCE)

	def move_up(self):
		new_y_coordinate = self.ycor() + MOVE_DISTANCE
		self.goto(self.xcor(), new_y_coordinate)

	def move_down(self):
		new_y_coordinate = self.ycor() - MOVE_DISTANCE
		self.goto(self.xcor(), new_y_coordinate)

	def goto_start_position(self):
		self.goto(STARTING_POSITION)

	def cross_finish_line(self):
		if self.ycor() > 280:
			return True
		else:
			return False
