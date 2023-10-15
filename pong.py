from turtle import Turtle

class Paddle1(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.speed("fastest")

    def go_up(self):
        new_y = self.ycor() + 10
        self.goto(-380, new_y)

    def go_down(self):
        new_y = self.ycor() - 10
        self.goto(-380, new_y)




class Paddle2(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.speed(100)

    def go_up(self):
        new_y = self.ycor() + 10
        self.goto(380, new_y)

    def go_down(self):
        new_y = self.ycor() - 10
        self.goto(380, new_y)

