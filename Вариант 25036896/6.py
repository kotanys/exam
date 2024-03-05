from turtle import *
k = 5
left(90)
speed(0)
for i in range(7):
    forward(50*k)
    right(90)
penup()
forward(10*k)
right(90)
forward(20*k)
pendown()
for i in range(4):
    forward(40*k)
    left(90)
penup()
tracer(0)
for x in range(-50, 60):
    for y in range(-60, 70):
        setpos(x*k, y*k)
        dot(2)
    
done()