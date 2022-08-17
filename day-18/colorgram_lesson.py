# import colorgram

# colors = colorgram.extract('./day-18/20_001.jpg', 30)

# color_list = []

# for col in colors:
#     rgb = col.rgb
#     color_list.append((rgb.r, rgb.g, rgb.b))

# print(color_list)

color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]

from turtle import Screen, Turtle, colormode, dot, right
import random
import turtle

tur = Turtle()

colormode(255)

tur.shape("circle")
tur.shapesize(0.2,0.2)
tur.color("red")
tur.speed('fast')
steps = 10
step = 50
dot_size = 20
tur.penup()
for i in range(steps):
    y = -steps * step / 2 + i*step
    for j in range(10):
        x = -steps * step / 2 + j*step
        tur.goto(x, y)
        tur.color(random.choice(color_list))
        tur.dot(dot_size)
        pass
screen = Screen()
screen.exitonclick()