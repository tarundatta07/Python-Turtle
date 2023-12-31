from turtle import Turtle


class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.color('white')
		self.penup()
		self.hideturtle()
		self.left_paddle_score  = 0
		self.right_paddle_score = 0
		self.update_scoreboard()

	def update_scoreboard(self):
		self.clear()
		self.goto(-100, 240)
		self.write(self.left_paddle_score, align='center', font=('Arial', 40, 'normal'))
		self.goto(100, 240)
		self.write(self.right_paddle_score, align='center', font=('Arial', 40, 'normal'))

	def left_paddle_scoreboard(self):
		self.left_paddle_score += 1
		self.update_scoreboard()

	def right_paddle_scoreboard(self):
		self.right_paddle_score += 1
		self.update_scoreboard()

