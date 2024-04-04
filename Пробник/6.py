from turtle import *
k=35
speed(0)
left(90)
for i in range(7):
    right(90)
    forward(3*k)
    for j in range(2):
        left(90)
        forward(3*k)
left(20)
for i in range(7):
    right(90)
    forward(3*k)
    for j in range(2):
        left(90)
        forward(3*k)

tracer(0)
penup()
for x in range(-10, 11):
    for y in range(-10, 11):
        setpos(x*k,y*k)
        dot(3)
done()