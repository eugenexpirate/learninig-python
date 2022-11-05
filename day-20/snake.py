from turtle import Turtle, Screen
from enum import IntEnum
import time
import random


class GameStatus(IntEnum):
    EXIT = 0
    START = 1
    RUN = 2
    GAME_OVER = 3
    PAUSED = 4

class PlayerActions(IntEnum):
    IDLE = 0
    LEFT = 1
    RIGHT = 2
    EXIT = 3
    PAUSE = 4

class SnakeGame:
    def __init__(self) -> None:
        self.status = GameStatus.START
        self.player_action = PlayerActions.IDLE
        self.init_screen()
        self.init_snake()
        self.init_bonus()
        self.init_frame()

        self.game_score = 0

    def init_snake(self):
        self.element_size = 10
        self.max_speed = 10
        self.min_speed = 3
        self.snake_speed = self.min_speed
        self.snake_segments = []
        for i in range(1,4):
            new_segment = Turtle(shape = "square")
            new_segment.width(10)
            new_segment.shapesize(0.5,0.5)
            new_segment.fillcolor("white")
            new_segment.setheading(0)
            new_segment.penup()
            new_segment.setpos(0-i*self.element_size, 0)
            self.snake_segments.append(new_segment)

    def init_bonus(self):
        self.bonus = Turtle(shape="circle")
        self.bonus.shapesize(0.5, 0.5)
        self.bonus.fillcolor("red")
        self.bonus.hideturtle()
        self.bonus_available = False

    def init_screen(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.title = "~={Snake Game}=~"
        self.screen.tracer(0)
        self.screen.bgcolor("black")
        self.screen.onkeypress(self.Exit, key="Escape")
        self.screen.onkeypress(self.SpeedUp, key="Up")
        self.screen.onkeypress(self.SpeedDown, key="Down")
        self.screen.onkeypress(self.change_direction_left, key="Left")
        self.screen.onkeypress(self.change_direction_right, key="Right")
        self.screen.onkeypress(self.StartGame, key="Return")
    
    def init_frame(self):
        self.frame = Turtle()
        f = self.frame
        f.hideturtle()
        f.pencolor("grey")
        f.pensize(width=2)
        f.penup()
        f.goto(-251, 251)
        f.pendown()
        f.goto(-251, -251)
        f.goto(251, -251)
        f.goto(251, 251)
        f.goto(-251, 251)
        
        self.caption = Turtle()
        c = self.caption
        c.hideturtle()
        c.penup()
        c.goto(0, 255)
        c.pencolor("grey")
        c.write("~={Snake Game}=~", align="center", font=('Courier New', 15, 'bold'))

        s = self.start_message = Turtle()
        s.hideturtle()
        s.penup()
        s.goto(0, -30)
        s.pencolor("grey")
        s.write("Press Enter to start the game.", align="center", font=("Courier New", 12, "bold"))

        r = self.results = Turtle()
        r.hideturtle()
        r.penup()
        r.goto(-251,-271)
        r.pencolor("grey")
        r.write("Score: 0", align="left", font=("Courier New", 12, "bold"))
    
    def random_bonus(self):
        if self.bonus_available: return
        x = y = 0
        check = True
        while check:
            x = random.randint(-24, 24)*10
            y = random.randint(-24, 24)*10
            check = False
            for segment in self.snake_segments:
                if segment.xcor() == x and segment.ycor() == y: check = True
        self.bonus.goto(x=x, y=y)
        self.bonus.showturtle()
        self.bonus_available = True

    def is_get_bonus(self) -> bool:
        x = self.snake_segments[0].xcor()
        y = self.snake_segments[0].ycor()
        if abs(x-self.bonus.xcor()) < 5  and abs(y-self.bonus.ycor())<5:
            self.bonus_available = False
            return True

    def add_score(self):
        self.game_score += 5
        self.results.clear()
        self.results.write(f"Score: {self.game_score}", align="left", font=("Courier New", 12, "bold"))
        if self.game_score > 30:
            self.snake_speed = 4
        if self.game_score > 60:
            self.snake_speed = 5
        if self.game_score > 90:
            self.snake_speed = 6
        if self.game_score > 120:
            self.snake_speed = 7
        if self.game_score > 150:
            self.snake_speed = 8
        if self.game_score > 180:
            self.snake_speed = 9
        if self.game_score > 210:
            self.snake_speed = 10

    def is_bit_yourself(self) -> bool:
        x = self.snake_segments[0].xcor()
        y = self.snake_segments[0].ycor()
        for segment in self.snake_segments[1:]:
            if abs(segment.xcor()-x)<5 and abs(segment.ycor()-y)<5:
                return True

        return False

    def is_bit_frame(self) -> bool:
        x = self.snake_segments[0].xcor()
        y = self.snake_segments[0].ycor()
        if x<=-250 or x>= 250 or y<=-250 or y>=250: return True

        return False

    def add_new_element(self):
        new_segment = Turtle(shape="square")
        new_segment.width(10)
        new_segment.shapesize(0.5, 0.5)
        new_segment.fillcolor("white")
        new_segment.penup()

        last_element = self.snake_segments[-1]
        heading = last_element.heading()
        x = last_element.xcor()
        y = last_element.ycor()
        if heading == 0: 
            x -= self.element_size
        if heading == 180:
            x += self.element_size
        if heading == 90:
            y -= self.element_size
        if heading == 270:
            y += self.element_size

        new_segment.setpos(x, y)
        new_segment.setheading(heading)
        self.snake_segments.append(new_segment)

    def move_snake(self):
        for i in range(0, len(self.snake_segments))[::-1]:
            self.snake_segments[i].forward(10)
            heading = self.snake_segments[i-1].heading()
            if i == 0: break
            self.snake_segments[i].setheading(heading)

    def change_direction_left(self):
        heading = self.snake_segments[0].heading()
        heading += 90
        heading %= 360
        self.snake_segments[0].setheading(heading)

    def change_direction_right(self):
        heading = self.snake_segments[0].heading()
        heading -= 90
        if heading < 0: heading += 360
        self.snake_segments[0].setheading(heading)
        
    def SpeedUp(self):
        if self.snake_speed < 10:
            self.snake_speed += 1

    def SpeedDown(self):
        if self.snake_speed > self.min_speed:
            self.snake_speed -= 1
    
    def StartGame(self):
        if self.status == GameStatus.GAME_OVER: 
            self.status = GameStatus.EXIT
            return

        self.status = GameStatus.RUN
        self.start_message.clear()
    
    def Exit(self):
        self.status = GameStatus.EXIT

    def Run(self) -> None:
        while self.status != GameStatus.EXIT:
            self.screen.listen()
            if self.status == GameStatus.RUN:
                self.random_bonus()
                self.screen.update()            
                time.sleep(0.5 / self.snake_speed)
                self.move_snake()
                if self.is_get_bonus():
                    self.add_new_element()
                    self.add_score()
                if self.is_bit_yourself() or self.is_bit_frame():
                    self.status = GameStatus.GAME_OVER
            if self.status == GameStatus.GAME_OVER:
                self.start_message.write(
                    f"Game over. Your score is {self.game_score}.", 
                    align="center",
                    font=("Courier New", 12, "normal")
                    )
            else:
                time.sleep(0.5 / self.snake_speed)
                self.screen.update() 

    def Start(self) -> None:
        # self.status = GameStatus.RUN
        self.Run()


game = SnakeGame()
game.Start()


