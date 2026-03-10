#Snake game project

from turtle import Turtle, Screen
import time
from snake import Snake
def moveForward():
    pass
screen = Screen()
screen.setup(width=600, height=600)         #Set screen height and width
screen.bgcolor('black')                     #Set background color of screen
screen.title("My Snake Game")               #Set title of the screen it will appear on screen titlebar
screen.tracer(0)                            # 0 value turns off the tracer and 1 turns it on
#Everything works fine but until we don't say update() method the screen will not show output
snake = Snake()
screen.listen()
screen.onkey(key="Up", fun=snake.moveUp)
screen.onkey(key="Down", fun=snake.movedown)
screen.onkey(key="Left", fun=snake.moveleft)
screen.onkey(key="Right", fun=snake.moveright)

                            #it will show everything that happend after tracer method
gameIsON = True

while gameIsON:
    screen.update()
    time.sleep(0.1)
    # for snakes in snakeDots:                  in this method snake will move segment by segment and direction will be changed
    #     snakes.forward(20)
    snake.move()

screen.exitonclick()