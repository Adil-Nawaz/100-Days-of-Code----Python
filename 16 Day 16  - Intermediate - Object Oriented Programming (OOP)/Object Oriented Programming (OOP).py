#How to use object oriented programming
# One method
# import turtle
# timmy = turtle.Turtle()
'''
# Second method
from turtle import Turtle, Screen     #imported two classes
timmy = Turtle()                      #created object
timmy.shape("turtle")                 #changed shape of turtle
timmy.color("blue")                   #Changed color of turtle
timmy.forward(100)                    #Move turtle fwd by 100 paces
my_Screen = Screen()                  #made screen object
print(my_Screen.canvheight)           #displayed screen object
my_Screen.exitonclick()               #screen will be closed on click only
'''

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pickachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)
table.align = 'l'   #alingment of table data
print(table)