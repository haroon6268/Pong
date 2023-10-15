from turtle import Screen
import time
from pong import Paddle1, Paddle2
from ball import Ball
from score import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.tracer(0)

player_1 = Paddle1()
player_1.goto(-380,0)

player_2 = Paddle2()
player_2.goto(380,0)


screen.listen()
screen.onkeypress(player_1.go_up, "w")
screen.onkeypress(player_1.go_down, "s")
screen.onkeypress(player_2.go_up, "i")
screen.onkeypress(player_2.go_down, "k")

ball = Ball()
score = Scoreboard()
score.update_score()

game = True
while game:
    ball_contact = False
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.reverse_y()

    if ball.distance(player_1) < 30 or ball.distance(player_2) < 30:
        ball_contact = True

    for _ in range(1):
        if ball_contact:
            ball.reverse_x()
            ball_contact = False

    #detects paddle




    #detecting going through wal
    if ball.xcor() < -400 or ball.xcor() > 400:
        ball.reverse_x()
        ball.reset()
        ball.move_speed = 0.1
        time.sleep(1)

    #detecting score
    if ball.xcor() > 390:
        score.player1_score()
    if ball.xcor() < -390:
        score.player2_score()



screen.exitonclick()
