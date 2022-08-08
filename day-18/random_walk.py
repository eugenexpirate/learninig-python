import random
from turtle import Screen, Turtle



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
        R = random.random()
        B = random.random()
        G = random.random()
        self._turtle.color(R, G, B)

    def _make_step(self):
        self.change_color()
        angle_orient = random.choice([0, 90, 180, 270])
        self._turtle.left(angle_orient)
        self._turtle.forward(self._step_len)
        

    def run(self):
        for _ in range(self._steps_count):
            self._make_step()



walker = RandomWalk(Turtle(), 30, 1000)
walker.run()

screen = Screen()
screen.exitonclick()