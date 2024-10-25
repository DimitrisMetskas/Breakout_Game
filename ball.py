from turtle import Turtle


class Ball(Turtle):
    # create ball
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # make the ball move
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # make the ball bounce at y
    def bouncey(self):
        self.y_move *= -1
        self.move_speed *= 0.93

    # make the ball bounce at x
    def bouncex(self):
        self.x_move *= -1

    # reset the ball to its initial position
    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bouncex()
