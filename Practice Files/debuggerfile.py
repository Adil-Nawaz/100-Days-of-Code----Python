
import turtle
turtle.colormode(255)
from turtle import Turtle, Screen

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (128, 0, 128), (0, 255, 255), 
          (255, 192, 203), (75, 0, 130), (60, 179, 113)]

def shapeBuilder(object, numberOfCorners):
    for _ in range(numberOfCorners):
        object.forward(100)
        object.right(360/numberOfCorners)

#Drawing geometrical shapes
tim2 = Turtle()
tim2.shape("turtle")
tim2.color(255,100,50)
colorNo = 0
for _ in range(3, 11):
    tim2.color(colors[colorNo])
    colorNo+=1
    shapeBuilder(tim2, _)
    
    
    
    

screen = Screen()
screen.exitonclick()