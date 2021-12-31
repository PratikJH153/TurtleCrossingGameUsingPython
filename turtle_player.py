from turtle import Turtle


class TurtlePlayer(Turtle):
    def __init__(self):
        super().__init__()
        self.difficulty = 0.1
        self.shape("turtle")
        self.penup()
        self.goto(0, -220)
        self.left(90)

    def up(self):
        self.forward(10)

    def reset_position(self):
        self.goto(0, -220)

    def increase_difficulty(self):
        self.difficulty *= 0.9
        self.reset_position()
