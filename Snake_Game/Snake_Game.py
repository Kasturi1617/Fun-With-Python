import turtle
import time
import snake
import food
import score

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(height=600, width=700)
screen.tracer(0)
screen.title("Snake Game :)")

snake = snake.Snake()
food = food.Food()
score = score.Score()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        if score.score >= 50:
            snake.extend()
        score.increase_score()

    # Detect collision with wall
    if snake.head.xcor()>345 or snake.head.xcor()< -345 or snake.head.ycor()>290 or snake.head.ycor()< -290:
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
