import turtle as t
from random import *

t.speed(100)
for i in range(1, 300):
    t.left(randint(0, 360))
    t.forward(randint(0, 50))
