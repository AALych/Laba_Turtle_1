import turtle
turtle.shape('triangle')
print('Введите количество вершин звезды')
n = int(input())
for i in range(0, n):
    turtle.forward(60)
    turtle.stamp()
    turtle.backward(60)
    turtle.left(360 / n)
