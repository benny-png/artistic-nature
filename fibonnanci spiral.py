import turtle

# Function to draw a colorful Fibonacci spiral
def draw_colorful_fibonacci_spiral(n):
    a, b = 0, 1
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    for _ in range(n):
        turtle.pencolor(colors[_ % len(colors)])  # Cycle through colors
        turtle.forward(b * 10)  # Adjust the factor for larger drawings
        turtle.left(90)
        a, b = b, a + b

# Set up the Turtle environment
turtle.speed(0)  # Fastest drawing speed
turtle.bgcolor("black")

# Move the turtle to the starting position
turtle.penup()
turtle.goto(-50, -50)
turtle.pendown()

# Draw the colorful Fibonacci spiral with a larger number of terms
draw_colorful_fibonacci_spiral(30000)  # Increase the number to make it larger

# Close the Turtle graphics window on click
turtle.exitonclick()
