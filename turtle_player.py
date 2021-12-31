from turtle import Turtle


class TurtlePlayer(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -220)
        self.left(90)

    def up(self):
        self.forward(10)

    def down(self):
        self.back(10)