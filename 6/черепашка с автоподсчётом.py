from turtle import *
speed(100)
k = 200 #! чем больше, тем лучше
begin_fill()
for i in range(12): #! заметь!! проходим по циклу ровно столько раз, сколько нужно, чтобы закончить фигуру
    right(60)
    forward(2 * k)
    right(60)
    forward(2 * k)
    right(270)
end_fill()
penup()
c = getcanvas() # получаем объект "холста", с помощью которого мы найдём, что где нарисовано
cnt = 0
for x in range(-15, 15):
    for y in range(-15, 15):
        a = c.find_overlapping(x*k, y*k, x*k, y*k) # находим, что было нарисовано в точке (x, y)
        if a == (5,): # если был нарисован только объект 5, значит здесь была только заливка
            cnt += 1
print(cnt)