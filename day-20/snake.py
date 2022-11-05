from turtle import Turtle, Screen
from enum import IntEnum
import time


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

    def add_new_element(self):
        new_segment = Turtle(shape = "square")
        new_segment.width(10)
        new_segment.shapesize(0.5,0.5)
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
        
    def SpeedUp(self):
        if self.snake_speed < 10:
            self.snake_speed += 1

    def SpeedDown(self):
        if self.snake_speed > self.min_speed:
            self.snake_speed -= 1

    def Exit(self):
        self.status = GameStatus.EXIT

    def Run(self) -> None:
        while self.status != GameStatus.EXIT:
            self.screen.update()
            self.screen.listen()
            time.sleep(0.5 / self.snake_speed)
            self.move_snake()
            # self.add_new_element()

    def Start(self) -> None:
        self.Run()

game = SnakeGame()
game.Start()


