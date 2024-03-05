from turtle import *
screensize(2000, 2000)
speed(0)
k = 50
right(45)
forward(4 * k)
for i in range(2):
    right(45)
    forward(7 * k)
    right(135)
    forward(4 * k)
penup()
tracer(0)
for x in range(-1, 7):
    for y in range(-10, 5):
        setpos(x*k, y*k)
        dot(3)
    
done()