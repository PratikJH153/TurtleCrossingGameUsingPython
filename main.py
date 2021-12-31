from turtle import Screen
import time

from turtle_player import TurtlePlayer
from car import Car
from level import Level

screen = Screen()
screen.colormode(255)
screen.setup(width=600, height=500)

screen.tracer(0)

turtle_player = TurtlePlayer()
level_board = Level()
car = Car()

screen.listen()
screen.onkeypress(key="Up", fun=turtle_player.up)


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(turtle_player.difficulty)
    car.create_car()

    for i in car.cars:
        if i.distance(turtle_player) <= 15:
            is_game_on = False
            level_board.game_over()

        if i.xcor() <= -300:
            i.hideturtle()
            car.cars.remove(i)
    car.move()

    if turtle_player.ycor() >= 230:
        level_board.update_level_board()
        turtle_player.increase_difficulty()


screen.exitonclick()
