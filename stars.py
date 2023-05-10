import turtle
import random

# Setari generale
t = turtle.Turtle()
t.speed(100)
t.hideturtle()
t.color("white", "yellow")

# Setari ecran
screen = turtle.Screen()
screen.bgcolor("#000000")

# Functie pentru desenare stea
def draw_star(turtle_obj, size):
    for _ in range(5):
        turtle_obj.forward(size)
        turtle_obj.left(216)


# Deseneaza stele de diferite marimi si in locatii aleatorii
for _ in range(70):
    x, y = random.randint(-400, 400), random.randint(-200, 200)
    star_size = random.randint(5, 25)

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    draw_star(t, star_size)
    t.end_fill()

# Update ecran dupa finalizare executie
screen.update()

# Mentine fereastra deschisa dupa finalizare executie
turtle.done()
