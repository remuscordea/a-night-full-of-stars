import turtle
import random

# Set up the turtle
t = turtle.Turtle()
t.speed(100)
t.hideturtle()

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("#000000")

# Use the tracer() method to speed up the drawing
# screen.tracer(0)

# Define the star colors (edge and fill)
t.color("white", "yellow")


# Define a function to draw a star
def draw_star(turtle_obj, size):
    for _ in range(5):
        turtle_obj.forward(size)
        turtle_obj.left(216)


# Draw multiple stars of varying sizes at random locations
for _ in range(70):
    x, y = random.randint(-400, 400), random.randint(-200, 200)
    star_size = random.randint(5, 25)

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    draw_star(t, star_size)
    t.end_fill()

# Update the screen once all stars have been drawn
screen.update()

# Keep the window open until the user closes it
turtle.done()
