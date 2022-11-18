from turtle import Screen, Turtle
from gamefield import GameField
from player import PongPlayer
from ball import PongBall
from score import ScoreNumber
import time
from datetime import datetime

class PongGame:
    START = 1
    MOVE = 2
    GAMEOVER = 6
    EXIT = 7
    INIT = 8
    
    def __init__(self) -> None:
        self.status = self.INIT
        self.screen = Screen()
        self.screen.tracer(0)
        self.screen.bgcolor("black")
        self.field = GameField()
        self.player1 = PongPlayer(x=-380)
        self.player2 = PongPlayer(x=380)
        self.ball = PongBall(speed=2)
        self.score1player = ScoreNumber(x=-50, y=260)
        self.score2player = ScoreNumber(x=50, y=260)
        self.score1value = 0
        self.score2value = 0
        self.timer = datetime.now()        
        
        
    def init(self):
        print("init()")
        self.screen.setup(width=850, height=650)    
        self.screen.onkey(self.player1.moveup, "w")
        self.screen.onkey(self.player1.movedown, "s")
        self.screen.onkeypress(lambda: self.exit(), "Escape")
        self.status = self.START
        return True

    def start(self):
        print("start()")
        self.status = self.MOVE
        return True
    
    def exit(self):
        print("exit()")
        self.status = self.EXIT
        return False

    def gameover(self):
        self.status = self.EXIT
        return True

    def move(self):
        self.ball.move()
        time.sleep(0.0025)
        ballx = self.ball.xcor()
        bally = self.ball.ycor()
        
        if ballx <= -380+15:
            playery = self.player1.ycor()
            diff = abs(playery - bally)
            if diff < self.player1.WIDTH/2:
                delta = 40*diff/self.player1.WIDTH
                if playery - bally < 0:
                    self.ball.setheading( 180 - self.ball.heading() + delta ) 
                else:
                    self.ball.setheading( 180 - self.ball.heading() - delta ) 
            else:
                if self.score2value < 9:
                    self.score2value += 1
                    self.score2player.setscore(self.score2value)
                    
                    self.ball.goto(self.player2.xcor()-16, self.player2.ycor())
                    self.ball.setheading(150)
                else:
                    self.status = self.GAMEOVER

        if ballx >= 380-15:
            playery = self.player2.ycor()
            diff = abs(playery - bally)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
            if diff < self.player1.WIDTH/2:
                delta = 40*diff/self.player1.WIDTH
                if playery - bally < 0:
                    self.ball.setheading( 180 - self.ball.heading() - delta ) 
                else:
                    self.ball.setheading( 180 - self.ball.heading() + delta )  
            else:
                if self.score1value < 9:
                    self.score1value += 1
                    self.score1player.setscore(self.score1value)
                    
                    self.ball.goto(self.player1.xcor()+16, self.player1.ycor())
                    self.ball.setheading(30)
                else:
                    self.status = self.GAMEOVER

        if (datetime.now() - self.timer).microseconds > 50000:
            if abs(self.player2.ycor()-self.ball.ycor())>20 and self.ball.xcor()>-100 :
                self.timer = datetime.now()
                if self.player2.ycor()-self.ball.ycor() < 0:
                    self.player2.moveup()
                else:
                    self.player2.movedown()
        return True

    actions = {
        START: start,
        EXIT: exit,
        INIT: init,
        GAMEOVER: gameover,
        MOVE: move,
    }

    def play(self):
        while self.actions[self.status](self):            
            self.screen.update()
            self.screen.listen()

        self.screen.exitonclick()