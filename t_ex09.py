import turtle as t
import math

t.shape('turtle')
R = 10
x = 1
t.penup()
t.goto(R, 0)
t.pendown()
def polygon(x):
    while x <= n:
        t.left((180 - 360 / n) / 2)
        t.left(360 / n)
        t.forward(2 * R * math.sin(math.pi/n))
        x += 1
        t.right((180 - 360 / n) / 2)
for n in range(3, 13):
    polygon(x)
    R += 18
    t.penup()
    t.goto(R, 0)
    t.pendown()




