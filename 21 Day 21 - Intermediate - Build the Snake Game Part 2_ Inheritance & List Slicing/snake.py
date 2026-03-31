from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.listofSnakes = []
        self.xpos = 0
        self.createSnake()
        self.head = self.listofSnakes[0]
        

    def createSnake(self):
        for snakes in range(3):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.pu()
            snake.goto(self.xpos,0)
            self.xpos-=20
            self.listofSnakes.append(snake)
    

    def move(self):
        for segments in range(len(self.listofSnakes)-1,0,-1):
            newX = self.listofSnakes[segments-1].xcor()
            newY = self.listofSnakes[segments-1].ycor()
            self.listofSnakes[segments].goto(newX,newY)
             #till this code all segments will be placed at one place because we are not moving the first segment fwd
        self.listofSnakes[0].forward(20) #this code will fwd first segment forward and above code will change the positions of other blocks
    
    def moveUp(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)
    def moveDown(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def moveLeft(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def moveRight(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)