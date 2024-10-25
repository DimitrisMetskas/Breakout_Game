from turtle import Turtle
import random

COLOR = ('blue', 'yellow', 'green', 'blue', 'pink', 'grey', 'purple')

POSSITIONS = [(-300, 330), (-200, 330), (-100, 330), (-0, 330),
              (100, 330), (200, 330), (300, 330),
              (-300, 305), (-200, 305), (-100, 305), (-0, 305),
              (100, 305), (200, 305), (300, 305),
              (-300, 280), (-200, 280), (-100, 280), (-0, 280),
              (100, 280), (200, 280), (300, 280),
              (-300, 255), (-200, 255), (-100, 255), (-0, 255),
              (100, 255), (200, 255), (300, 255),
              (-300, 230), (-200, 230), (-100, 230), (-0, 230),
              (100, 230), (200, 230), (300, 230),
              ]


class Brick():
    def __init__(self):
        self.wall = []
        self.create_briks()

    # create the brick wall
    def create_briks(self):
        for position in POSSITIONS:
            self.add_brks(position)

    # add all the bricks at brick wall
    def add_brks(self, position):
        brik = Turtle()
        brik.penup()
        brik.shape("square")
        brik.shapesize(stretch_wid=1, stretch_len=4.8)
        brik.color(random.choice(COLOR))
        brik.goto(position)
        self.wall.append(brik)

    # remove a specific brick from the wall list
    def delete(self, destroyed):
        self.wall.remove(destroyed)
        destroyed.hideturtle()

