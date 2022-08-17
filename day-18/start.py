from turtle import Screen, Turtle, forward, right
import random

timmy = Turtle()

def draw_dash_line(len: int, dashes: int):
    if dashes == 1: 
        timmy.forward(len)
        return

    if dashes < 1: return

    whites = dashes - 1
    total = dashes + whites

    line_size = len / total
    
    path = 0
    is_dash = True
    while path < len:
        if is_dash:
            is_dash = False
            timmy.pendown()
            if (path + line_size) > len:
                line_size = len - path
            timmy.forward(line_size)
        else:
            timmy.penup()
            is_dash = True
            timmy.forward(line_size)
        path += line_size

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    timmy.color(R, G, B)
    

timmy.shape("circle")
timmy.shapesize(0.2,0.2)
timmy.color("red")

# draw_dash_line(100,8)
# for i in range(0,3):
#     timmy.left(90)
#     draw_dash_line(100, 8)

for coners in range(3,12):
    change_color()
    for sides in range(0,coners):
        timmy.forward(100)
        timmy.right(360/coners)

screen = Screen()
screen.exitonclick()

