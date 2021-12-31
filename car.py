from turtle import Turtle
import random


class Car:
    def __init__(self):
        self.cars = []

    def create_car(self):
        if random.randint(1, 6) == 1:
            t = Turtle("square")
            t.color(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
            t.penup()
            t.goto(310, random.randint(-160, 160))
            t.shapesize(stretch_wid=0.6, stretch_len=1.2)
            t.left(180)
            self.cars.append(t)

    def move(self):
        for car in self.cars:
            car.forward(5)
