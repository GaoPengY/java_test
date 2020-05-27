from turtle import *
from random import random,randint

sc = Screen()
w,h = 800,600
sc.setup(w,h)
sc.title("星空")
sc.bgcolor("black")
sc.mode("logo")
sc.delay(0)

t = Turtle(visible = False,shape = "circle")
t.pencolor("white")
t.fillcolor("white")
t.penup()
t.setheading(-90)
t.goto(w/2,randint(-h/2,h/2))

stars = []
for x in range(360):
    star = t.clone()
    s = random()/3
    star.shapesize(s,s)
    star.speed(int(s*9))
    star.setx(w/2+randint(1,w))
    star.sety(randint(-h/2,h/2))
    star.showturtle()
    stars.append(star)

while True:
    for x in stars:
        x.setx(x.xcor() - 3*x.speed())
    if x.xcor() < -w/2:
        x.hideturtle()
        x.setx(w/2+randint(1,w))
        x.sety(randint(-h/2,h/2))
        x.showturtle()