from turtle import Turtle

class PongBall(Turtle):
    def __init__(self, speed: float = 1) -> None:
        super().__init__()
        super().shape("circle")
        super().pencolor("white")
        super().penup()
        super().shapesize(0.5, 0.5, 0)
        super().color("white")
        super().speed("fastest")
        super().setheading(30)
        self.speed = speed
        
    def move(self):
        x = super().xcor()
        y = super().ycor()
        if x+5 >= 400:
            super().setheading( 180 - super().heading() )

        if x-5 <= -400:
            super().setheading( 180 - super().heading() ) 

        if y+5 >= 300:
            super().setheading( 360 - super().heading() ) 
        
        if y-5 <= -300:
            super().setheading( 360 - super().heading() ) 

        super().forward(self.speed)
