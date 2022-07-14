import turtle
import random

turtle.colormode(255)
MOVE_DISTANCE = 10


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)
    return new_color


class Car():

    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_DISTANCE

    def create_car(self):
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            new_car = turtle.Turtle("square")
            new_car.color(random_color())
            new_car.penup()
            new_car.goto(320, random.randint(-250, 250))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_DISTANCE
