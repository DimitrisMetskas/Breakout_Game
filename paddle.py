from turtle import Turtle


class Paddle():

    def __init__(self):
        self.paddle()

    # create the paddle
    def paddle(self):
        self.mypaddle = Turtle()
        self.mypaddle.penup()
        self.mypaddle.shape("square")
        self.mypaddle.shapesize(stretch_wid=1, stretch_len=6)
        self.mypaddle.color("white")
        self.mypaddle.goto(0, -320)

    # make it go right
    def mypaddle_right(self):
        if self.mypaddle.xcor() < 280:
            new_x = self.mypaddle.xcor() + 20
            self.mypaddle.goto(new_x, self.mypaddle.ycor())

    # make it go left
    def mypaddle_left(self):
        if self.mypaddle.xcor() > - 280:
            new_x = self.mypaddle.xcor() - 20
            self.mypaddle.goto(new_x, self.mypaddle.ycor())
