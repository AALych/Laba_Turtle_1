from random import *
import turtle as t

t.up()
t.goto(-200, 200)
t.down()
for i in range (4):
    t.forward(400)
    t.right(90)
t.hideturtle()

number_of_turtles = 20

pool = [t.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(200)
    unit.color('red')
    unit.turtlesize(0.5, 0.5)
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.seth(randint(0, 360))
            
while True:
    for unit in pool:
        unit.forward(randint(1, 10))
        if abs(unit.xcor()) >= 200:
            unit.seth(180 - unit.heading())
            unit.forward(10)
        if abs(unit.ycor()) >= 200:
            unit.seth(360 - unit.heading())
            unit.forward(10)
