from turtle import Screen, Turtle, colormode, right
import random

tur = Turtle()

colormode(255)

tur.shape("circle")
tur.shapesize(0.2,0.2)
tur.color("red")
tur.speed('fastest')
circles = 50
for i in range(0, 360, int(360/circles) ):
    R = random.randint(0,255)
    B = random.randint(0,255)
    G = random.randint(0,255)
    tur.color(R, G, B)
    tur.circle(100)
    tur.left(360/circles)

screen = Screen()
screen.exitonclick()

