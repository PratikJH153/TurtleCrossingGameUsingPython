from turtle import Screen
from turtle_player import TurtlePlayer

screen = Screen()
screen.setup(width=600, height=500)

screen.tracer(0)

turtle_player = TurtlePlayer()

screen.listen()
screen.onkeypress(key="Up", fun=turtle_player.up)
screen.onkeypress(key="Down", fun=turtle_player.down)

is_game_on = True
while is_game_on:
    screen.update()

screen.exitonclick()
