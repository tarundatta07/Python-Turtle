from turtle import Turtle


class Ball(Turtle):

	def __init__(self):
		super().__init__()
		self.shape('circle')
		self.color('red')
		self.penup()
		self.x_move = 10
		self.y_move = 10
		self.move_ball_speed = 0.1

	def move_ball(self):
		new_x_coordinate = self.xcor() + self.x_move
		new_y_coordinate = self.ycor() + self.y_move
		self.goto(new_x_coordinate, new_y_coordinate)

	def toggle_ball_y_direction(self):
		self.y_move *= -1

	def toggle_ball_x_direction(self):
		self.x_move *= -1
		self.move_ball_speed *= 0.9

	def reset_ball(self):
		self.goto(0,0)
		self.toggle_ball_x_direction()
		self.move_ball_speed = 0.1