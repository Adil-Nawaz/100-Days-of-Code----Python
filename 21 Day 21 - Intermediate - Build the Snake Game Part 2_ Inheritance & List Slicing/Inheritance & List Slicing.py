'''
#Inheritance

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("Inhale, Exhale")


class Fish (Animal):
    def __init__(self):
        super().__init__()    #inherit everything from parent or super class
    
    def swim(self):
        print("Swimming in water")

    def breath(self):      #override parent method
        super().breath()       #do everything that is inside parent method
        print("doing this underwater")   #now do something new in addition to parent method

nemo = Fish()
nemo.swim()  #Local method
nemo.breath() #inherited method
print(nemo.num_eyes)   #Inherited attribute
'''

from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()

screen.listen()
screen.onkey(key="Up", fun=snake.moveUp)
screen.onkey(key="Down", fun=snake.moveDown)
screen.onkey(key="Left", fun=snake.moveLeft)
screen.onkey(key="Right", fun=snake.moveRight)

gameIsON = True
while gameIsON:
    screen.update()
    time.sleep(0.1)
    # for snakes in snakeSegmentsList:
    #     snakes.forward(20)
    snake.move()










screen.exitonclick()