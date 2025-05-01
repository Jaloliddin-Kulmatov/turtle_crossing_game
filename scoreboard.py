from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(). __init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.change_score()
    def change_score(self):
        self.clear()
        self.goto(-230,250)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
