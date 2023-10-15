from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.penup()
        self.hideturtle()
        self.goto(-100, 250)
        self.update_score()
        self.color("white")

    def update_score(self):
        self.goto(-100, 250)
        self.write(self.score1, align="center", font=("Arial", 50, "normal"))
        self.goto(100, 250)
        self.write(self.score2, align="center", font=("Arial", 50, "normal"))

    def player2_score(self):
        self.score2 += 1
        self.clear()
        self.update_score()

    def player1_score(self):
        self.score1 += 1
        self.clear()
        self.update_score()
