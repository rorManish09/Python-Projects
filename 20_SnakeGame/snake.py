from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):

        self.all_snake_segments = []

        self.create_snake()
        self.head = self.all_snake_segments[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)
    def add_segment(self,pos):
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.goto(pos)
        self.all_snake_segments.append(snake)

    def extend(self):
        self.add_segment(self.all_snake_segments[-1].pos())
    def move(self):
        for seg_num in range(len(self.all_snake_segments) - 1, 0, -1):
            new_x = self.all_snake_segments[seg_num - 1].xcor()
            new_y = self.all_snake_segments[seg_num - 1].ycor()
            self.all_snake_segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE)

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

