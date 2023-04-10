import random
from turtle import Turtle, Screen

is_race_on = True


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make  your bet", prompt="Which turtle will win the race? Enter a  color: ")

turtle_color = ["red", "blue", "black", "green", "purple", "yellow"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_color[index])
    new_turtle.penup()
    new_turtle.goto(x=-200, y=y_positions[index])
    all_turtle.append(new_turtle)


if user_bet:

    is_race_on = True


while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Won! The {winning_color} turtle is the winner !")
            else:
                print(f"You Lost! The {winning_color} turtle is the winner !")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

print(user_bet)
screen.exitonclick()
