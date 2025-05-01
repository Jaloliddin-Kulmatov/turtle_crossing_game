import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.onkey(key="Up", fun= player.move)
screen.onkey(key="w", fun= player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    if player.ycor() > 280:
       player.restart_position()
       scoreboard.score += 1
       scoreboard.change_score()
       car.level_up()

    for car_instance in car.all_cars:
        if player.distance(car_instance) < 25:
            scoreboard.game_over()
            game_is_on = False



screen.exitonclick()