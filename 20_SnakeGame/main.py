# importing classes
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")

screen.title("My snake game")

our_snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(our_snake.up, "Up")
screen.onkey(our_snake.down, "Down")
screen.onkey(our_snake.left, "Left")
screen.onkey(our_snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.08)
    our_snake.move()

    #Detect collision
    if our_snake.head.distance(food)<15:
       food.refresh()
       scoreboard.increase_score()
       our_snake.extend()

    #Detect collision with wall:

    if our_snake.head.xcor() > 280 or  our_snake.head.ycor() > 280:

        game_is_on = False
        scoreboard.game_over()

    if our_snake.head.xcor() < -290 or our_snake.head.ycor()<-290:

        game_is_on = False
        scoreboard.game_over()

#detect collison with tail

    for segments in our_snake.all_snake_segments:
        if segments == our_snake.head:
            pass

        elif our_snake.head.distance(segments)< 10:
            game_is_on = False
            scoreboard.game_over()

#if head collidde with any segment in tail

        # trigger game_over


screen.exitonclick()