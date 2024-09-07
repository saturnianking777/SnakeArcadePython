from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game 101")
screen.tracer(0)

game_is_on = True

snake = Snake()
food = Food()
score = Score()

name = screen.textinput("Score storage", "Enter your name")

screen.onkey(snake.up, "Up")
screen.onkey(snake.rgt, "Right")
screen.onkey(snake.down, "Down")
screen.onkey(snake.lft, "Left")

while game_is_on:
    screen.listen()
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # checks collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # checks collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        time.sleep(1)
        score.reset(name)
        cont = screen.textinput("Continue?", "Y/N")
        if cont == 'N':
            screen.bye()
            break
        snake.reset()

    # detects collision with own tail
    if snake.collision():
        time.sleep(1)
        score.reset(name)
        cont = screen.textinput("Continue?", "Y/N")
        if cont == 'N':
            screen.bye()
            break
        snake.reset()
