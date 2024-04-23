import turtle

# Function to draw a Koch snowflake
def koch_snowflake(turtle, order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(turtle, order - 1, size / 3)
            turtle.left(angle)

# Set up the Turtle environment
turtle.speed(0)  # Fastest drawing speed
turtle.bgcolor("black")
turtle.color("blue")

# Move the turtle to the starting position
turtle.penup()
turtle.goto(-150, 90)
turtle.pendown()

# Draw the Koch snowflake
for _ in range(3):
    koch_snowflake(turtle, 4, 300)
    turtle.right(120)

# Close the Turtle graphics window on click
turtle.exitonclick()
