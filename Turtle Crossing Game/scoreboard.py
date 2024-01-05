from turtle import Turtle

FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f'Level: {self.level}', align='left', font=FONT)

    def increase_score(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write('GAME OVER', align='center', font=FONT)