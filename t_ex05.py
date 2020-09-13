import turtle
turtle.shape('turtle')
for i in range(1, 11):
    turtle.forward(10*i)
    turtle.left(90)
    for k in range(0,3):
        turtle.forward(20*i)
        turtle.left(90)
    turtle.forward(10*i)
    turtle.right(90)
    turtle.penup()
    turtle.forward(10)
    turtle.left(90)
    turtle.pendown()
