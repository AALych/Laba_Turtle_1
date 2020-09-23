import turtle
turtle.shape('turtle')
a = 10
turtle.left(90)
for k in range(0, 5):
    for i in range(0, 60):
        turtle.forward(a)
        turtle.left(6)
    for i in range(0, 60):
        turtle.forward(a)
        turtle.right(6)
    a += 2
    
