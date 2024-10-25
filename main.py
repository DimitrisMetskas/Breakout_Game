from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from bricks import Brick

screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

whitepaddle = Paddle()
theball = Ball()
bricks = Brick()

screen.listen()
screen.onkey(whitepaddle.mypaddle_right, "Right")
screen.onkey(whitepaddle.mypaddle_left, "Left")

is_on = True
while is_on:

    screen.update()
    time.sleep(theball.move_speed)
    theball.move()
    # detect bounce with right/left wall
    if theball.xcor() >= 330 or theball.xcor() <= -330:
        theball.bouncex()

    # detect bounce with top/bot wall
    if theball.ycor() >= 350:
        theball.bouncey()

    #detect collition with paddle
    if theball.distance(whitepaddle.mypaddle) < 50 and theball.ycor() <= -300:
        theball.bouncey()

    #detect paddle misses
    if theball.ycor() < -340:
        theball.reset()
        bricks.create_briks()
        # scoreboard.l_point()

    #detect collition with brick
    for b in bricks.wall:
        if theball.distance(b) < 45 and theball.ycor() >= b.ycor() - 10:
            theball.bouncey()
            bricks.delete(b)

screen.exitonclick()
