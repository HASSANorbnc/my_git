import random
from turtle import Turtle,Screen
window=Screen()
window.title("welcomm to run turtle")
window.setup(500,400)
colors=("red","blue","green")
y_positions=(-70,0,70)
Turtles=[]
user_bet =window.textinput("make your bet","Guess the winner:\ntype a color: red,blue,green")
for i in range(3):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-200,y=y_positions[i])
    Turtles.append(new_turtle)
def race_turtles():
    is_race=True
    while is_race:
        for turtle in Turtles: 
            if turtle.xcor()>280:
                is_race=False
                winning_color=turtle.pencolor()
                display_result(winning_color)
            else:
                turtle.forward(random.randint(1,15))
def display_result(winning_color):
    result_turtle=Turtle()
    result_turtle.hideturtle()
    result_turtle.penup()
    result_turtle.goto(0,0)
    result_turtle.pendown()
    if winning_color==user_bet:
        window.bgcolor("green")
        result_turtle.color("white")
        result_turtle.write("you win!",align="center",font=("Arial",28,"normal"))
    else:
        window.bgcolor("medium violet red")
        result_turtle.color("white")
        result_turtle.write("you lose ",align="center",font=("Arial",28,"normal"))    
race_turtles()
window.exitonclick()
