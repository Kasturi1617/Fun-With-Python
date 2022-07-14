from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)
ball = Ball()
left_score = Score(-100, 250)
right_score = Score(100, 250)

screen.listen()
screen.onkey(key="Up", fun=right_paddle.go_up)
screen.onkey(key="Down", fun=right_paddle.go_down)
screen.onkey(key="W", fun=left_paddle.go_up)
screen.onkey(key="S", fun=left_paddle.go_down)

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.go_to_position()

    # Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 :
        ball.bounce_x()
        right_score.update_scoreboard()

    # Detect collision with left paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        left_score.update_scoreboard()

    # Detect if right paddle misses ball
    if ball.xcor() > 380:
        ball.reset()
        left_score.update_scoreboard()

    # Detect if left paddle misses ball
    if ball.xcor() < -380:
        ball.reset()
        right_score.update_scoreboard()

screen.exitonclick()
