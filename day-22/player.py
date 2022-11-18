from turtle import Turtle

class PongPlayer(Turtle):
    WIDTH = 100

    def __init__(self, x: int = 0, y: int = 0) -> None:
        super().__init__()
        super().shape("square")
        super().speed('fastest')
        super().color('white')
        super().pensize(0)
        super().shapesize(self.WIDTH/20, 0.5, 0) # 4*20 = 80; 0.5*20 = 10
        super().penup()
        super().goto(x, y)

    def moveup(self):
        y = super().ycor()
        if y+self.WIDTH/2 >= 300:
            return
        super().sety(y+10)

    def movedown(self):
        y = super().ycor()
        if y-self.WIDTH/2 <= -300:
            return
        super().sety(y-10)