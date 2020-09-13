import turtle
turtle.shape('turtle')
angle_rad = 0.1
angle_degr = angle_rad * (180 / 3.14)
for i in range (0,1000):
    r = angle_rad
    turtle.forward(r)
    turtle.left(angle_degr)
    angle_rad += 0.1
    r += r
