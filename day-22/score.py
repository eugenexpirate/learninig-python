from turtle import Turtle

SCOREVALUES = [
    [True, False, True, True, True, True, True],        # 0
    [False, False, False, False, False, True, True],    # 1
    [True, True, True, False, True, True, False],       # 2
    [True, True, True, False, False, True, True],       # 3
    [False, True, False, True, False, True, True],      # 4
    [True, True, True, True, False, False, True],       # 5
    [True, True, True, True, True, False, True],        # 6
    [True, False, False, False, False, True, True],     # 7
    [True, True, True, True, True, True, True],         # 8
    [True, True, True, True, False, True, True]         # 9
]

class ScoreNumber:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.sections = {
            "TOP":  Turtle(),
            "MID":  Turtle(),
            "LOW":  Turtle(),
            "LH":   Turtle(),
            "LL":   Turtle(),
            "RH":   Turtle(),
            "RL":   Turtle()
        }
        self.x = x
        self.y = y
        
        self.init()
    

    SEGMENTW = 30.0
    SEGMENTH = 5.0

    def init(self):
        for turt in self.sections.values():
            turt.color('white')
            turt.speed('fastest')
            turt.shape("square")
            turt.pensize(0)
            turt.penup()
            turt.shapesize(self.SEGMENTW/20, self.SEGMENTH/20, 0) 

        self.sections["MID"].goto(self.x, self.y)
        self.sections["MID"].setheading(90)

        self.sections["TOP"].goto(self.x, self.y+self.SEGMENTW-self.SEGMENTH)
        self.sections["TOP"].setheading(90)

        self.sections["LOW"].goto(self.x, self.y-self.SEGMENTW+self.SEGMENTH)
        self.sections["LOW"].setheading(90)

        shiftx = (self.SEGMENTW-self.SEGMENTH)/2
        shifty = shiftx
        self.sections["LH"].goto(self.x-shiftx, self.y+shifty)
        self.sections["LL"].goto(self.x-shiftx, self.y-shifty)
        self.sections["RH"].goto(self.x+shiftx, self.y+shifty)
        self.sections["RL"].goto(self.x+shiftx, self.y-shifty)

        self.sections["MID"].hideturtle()

    def setscore(self, score: int = 0):
        if score < 0 or score > 9: self.setscore(0)
        index = 0
        for section in self.sections.values():
            if SCOREVALUES[score][index]:
                section.showturtle()
            else:
                section.hideturtle()
            index += 1
        
            
