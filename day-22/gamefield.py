from turtle import Turtle

class GameField(Turtle):
    def __init__(self,) -> None:
        super().__init__()
        self.paint()
    
    def paint(self):
        super().penup()
        super().speed("fastest")
        super().hideturtle()
        super().width(5)
        super().pencolor("white")
        super().goto(-400, 300)
        super().pendown()
        super().goto(400, 300)
        super().goto(400, -300)
        super().goto(-400, -300)
        super().goto(-400, 300)
        super().penup()
        super().goto(0, 300)
        super().setheading(270)
        paint = True
        super().width(2)
        while super().ycor() > -300:
            if paint:
                paint = False
                super().pendown()
                super().forward(20)
            else:
                paint = True
                super().penup()
                super().forward(20)

