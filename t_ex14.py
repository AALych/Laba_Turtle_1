import turtle as t

def star(n, a):
    t.penup()
    t.left(180 / n)
    t.pendown()
    for i in range(1, n + 1):
        t.forward(a)
        t.left(180 - 180 / n)

star(5, 100)
t.penup()
t.goto(200, 0)
t.pendown()
star(11, 100)

