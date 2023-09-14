from turtle import Turtle

ALIGNMENT = 'center'
FONT_STYLE = ('Arial', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=FONT_STYLE)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_is_over(self):
        self.goto(x=0, y=0)
        self.write("Game Over", align=ALIGNMENT, font=FONT_STYLE)
