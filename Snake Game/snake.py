from turtle import Turtle

SNAKE_STARING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:

    def __init__(self):
        self.combine_blocks = []
        self.creating_snake()
        self.head = self.combine_blocks[0]

    # # =============== CREATING SNAKE ===================#
    def creating_snake(self):
        for position in SNAKE_STARING_POSITION:
            single_block = Turtle(shape='square')
            single_block.color('white')
            single_block.penup()
            single_block.goto(position)
            self.combine_blocks.append(single_block)

    # =============== MOVING SNAKE ===================#
    def move_snake(self):
        for segment_num in range(len(self.combine_blocks) - 1, 0, -1):
            new_x_coordinate = self.combine_blocks[segment_num - 1].xcor()
            new_y_coordinate = self.combine_blocks[segment_num - 1].ycor()
            self.combine_blocks[segment_num].goto(new_x_coordinate, new_y_coordinate)
        self.head.forward(SNAKE_MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
