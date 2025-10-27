import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.speed("fastest")
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    random_color = (r, g, b)
    return random_color
    


def draw_spirograph(radius,angle_gap, circle_size):
    tim.pensize(circle_size)
    for i in range(int(360/angle_gap)):
        tim.circle(radius)
        tim.setheading(tim.heading() + angle_gap)
        tim.pencolor(random_color()) 
        

draw_spirograph(int(input("Enter the radius: ")), int(input("Enter the angle gap: ")), int(input("Enter the circle size: ")))

screen =  Screen()
screen.exitonclick()