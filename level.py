from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-280, 210)
        self.update_level_board()

    def update_level_board(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Courier", 16, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 16, "bold"))
