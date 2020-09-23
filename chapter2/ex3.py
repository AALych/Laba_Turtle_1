import turtle as t

with open('config.txt') as file:
    Numb = []
    for j in range(10):
        s = file.readline()
        s = s.rstrip()
        a = list(map(int, s.split()))
        p = [(0 , 0)] * (int(len(a) / 2))
        for i in range(len(p)):
            p[i] = a[i*2], a[i*2 + 1]
        Numb.append(p)
        
def number_draw(n,m):
     t.penup()
     t.goto(Numb[n][0][0] + 50 * m, Numb[n][0][1])
     t.pendown()
     for x, y in Numb[n]:
               t.goto(x + 50 * m, y)
def ind_draw(index):
     No = 1
     for k in index:
          number_draw(int(k), No)
          No += 1

No = 1
ind_draw('141700')
