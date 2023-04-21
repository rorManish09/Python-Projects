from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.shape("circle")

        self.color("white")
        self.goto(0, 0)
        self.x_move = 1
        self.y_move = 1


    def move(self):

        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):

        self.y_move *= -1

    def bounce_x(self):

        self.x_move *=-1

    def reset_postion(self):

        self.goto(0,0)
        self.bounce_x()