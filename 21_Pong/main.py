import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
# screen setup

screen = Screen()
screen.setup(height=600, width=800)

screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
# Setup paddle


l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))


# Ball

ball = Ball()
scoreboard =Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "W")
screen.onkey(l_paddle.go_down, "S")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.update()
is_game_on = True

while is_game_on:
    time.sleep(0.005)
    screen.update()
    ball.move()

# detect collision
    if ball.ycor()>280 or ball.ycor() < -280:
        ball.bounce_y()



# detect coll
    if ball.distance(r_paddle) < 60 and ball.xcor() > 340 or ball.distance(l_paddle) <60 and ball.xcor()<-340:
        ball.bounce_x()

# detect while ball misses the paddle

    if  ball.xcor() > 380 :
        scoreboard.l_point()
        ball.reset_postion()

    if ball.xcor() < - 380:
        scoreboard.r_point()
        ball.reset_postion()
screen.exitonclick()
