from turtle import *

speed(10)
color("yellow")
bgcolor("black")
b =200

screen = Screen()

# Set the screen to full screen mode
screen.setup(width=1.0, height=1.0)
while b >0:
    left(b)
    forward(b*3)
    b = b-1
