import random
from turtle import Screen, Turtle
import turtle



class RandomWalk:
    def __init__(self, tur: Turtle, step_len: int, steps_count: int) -> None:
        self._turtle = tur
        self._step_len = step_len
        self._steps_count = steps_count
        self._turtle.shape('circle')
        self._turtle.shapesize(0.5,0.5)
        self._turtle.pensize(5)
        self._turtle.speed(0)
    
    def change_color(self):
        R = random.randint(0,255)
        B = random.randint(0,255)
        G = random.randint(0,255)
        self._turtle.color(R, G, B)

    def _make_step(self):
        self.change_color()
        angle_orient = random.choice([0, 90, 180, 270])
        self._turtle.setheading(angle_orient)
        self._turtle.forward(self._step_len)
        

    def run(self):
        for _ in range(self._steps_count):
            self._make_step()


turtle.colormode(255)
walker = RandomWalk(Turtle(), 30, 200)
walker.run()

screen = Screen()
screen.exitonclick()