from turtle import Screen, Turtle, pencolor, pensize
from random import randint

rainbow = [
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'indigo',
    'violet'
]

class RaceGame:
    def __init__(self) -> None:
        self.max_speed = 20
        
        self.field_w = 400
        self.field_h = 300

        self.init()

    def run(self) -> None:
        temp_color = ""
        while temp_color not in rainbow:
            temp_color = self.screen.textinput(title="Choose your bet color", prompt = f"Type one of the color {rainbow}").lower()
        self.color_choose = temp_color
        self.racers[temp_color].pen(pencolor="black", pensize=3)

        while self.game_continue():
            self.move_racers()
            self.put_racers()


        winner = self.get_winner()
        self.racers[winner].write("Winner!")
        if self.color_choose == winner:
            Turtle().write("You win!")
        else:
            Turtle().write("You loose!")

        

        self.screen.exitonclick()

    def put_racers(self) -> None:
        for color in rainbow:
            self.racers[color].goto(x=self.racers_coord[color].x, y=self.racers_coord[color].y)

    def move_racers(self):
        for color in rainbow:
            self.racers_coord[color].x += randint(5,self.max_speed)

    def get_winner(self) -> str:
        winner = rainbow[0]
        winner_x = self.racers_coord[winner].x
        for color in rainbow:
            if self.racers_coord[color].x > winner_x:
                winner_x = self.racers_coord[color].x
                winner = color

        return winner

    def game_continue(self) -> bool:
        for color in rainbow:
            if self.racers_coord[color].x >= int(self.field_w/2):
                return False
        return True

    class coord:
        def __init__(self) -> None:
            self.x = 0
            self.y = 0

    def init(self) -> None:
        self.screen = Screen()
        self.screen.setup(width=500, height=400)
        self.racers = {}
        self.racers_coord = {}
        start_x = int(- self.field_w / 2)
        start_y = int(self.field_h / 2)
        shift_y = 0
        for color in rainbow:
            self.racers[color] = Turtle(shape="turtle")
            self.racers[color].color(color)
            self.racers_coord[color] = self.coord()
            self.racers_coord[color].x = start_x
            self.racers_coord[color].y = start_y - shift_y
            shift_y += int(self.field_h / (len(rainbow)-1))
            self.racers[color].penup()

        finish_line = Turtle(visible=False)
        finish_line.pen(pencolor='black', pensize=5)
        finish_line.penup()
        finish_line.goto(x=int(self.field_w/2), y= int(self.field_h/2)+10)
        finish_line.pendown()
        finish_line.goto(x=int(self.field_w/2), y= -int(self.field_h/2)-10)
        
        self.put_racers()

game = RaceGame()
game.run()