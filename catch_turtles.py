from turtle import *
from random import randint
import time

def draw_boundaries(width, height):
    boundary = Turtle()
    boundary.penup()
    boundary.goto(-width, -height)
    boundary.pendown()
    boundary.color('black')
    boundary.width(2)
    for i in range(2):
        boundary.forward(width * 2)
        boundary.left(90)
        boundary.forward(height * 2)
        boundary.left(90)
    boundary.hideturtle()

def create_timer():
    timer = Turtle()
    timer.penup()
    timer.goto(-w + 30 , h + 10)  
    timer.hideturtle()
    return timer

def update_timer(timer, seconds):
    timer.clear()
    timer.write(f"Time: {seconds}s", font=('Arial', 16, 'normal'))

title("Catch the turtles")
w = 300
h = 250

# Draw boundaries
draw_boundaries(w, h)

# Create and set up the timer
timer = create_timer()

t1 = Turtle()
t1.color('blue')
t1.width(5)
t1.shape('turtle')
t2 = Turtle()
t2.color('green')
t2.width(5)
t2.left(120)
t2.shape('turtle')
t3 = Turtle()
t3.color('red')
t3.width(5)
t3.left(-120)
t3.shape('turtle')
t1.penup()
t2.penup()
t3.penup()

def catch1(x, y):
    t1.penup()
    t1.goto(randint(-100,100),randint(-100,100))
    t1.left(randint(0, 180))

def catch2(x, y):
    t2.penup()
    t2.goto(randint(-50,50),randint(-50,50))
    t2.left(randint(0, 180))

def catch3(x, y):
    t3.penup()
    t3.goto(randint(-50,50),randint(-50,50))
    t3.left(randint(0, 180))

def gameFinished(t1, t2, t3):
    t1_outside = abs(t1.xcor()) > w or abs(t1.ycor()) > h
    t2_outside = abs(t2.xcor()) > w or abs(t2.ycor()) > h
    t3_outside = abs(t3.xcor()) > w or abs(t3.ycor()) > h
    isOutside = t1_outside or t2_outside or t3_outside
    return isOutside

t1.onclick(catch1)
t2.onclick(catch2)
t3.onclick(catch3)

start_time = time.time()
while not gameFinished(t1, t2, t3):
    t1.forward(7)
    t2.forward(randint(3,8))
    t3.forward(randint(4,6))
    
    # Update timer
    elapsed_time = int(time.time() - start_time)
    update_timer(timer, elapsed_time)
    
    time.sleep(0.1)

# Game over
final_time = int(time.time() - start_time)
update_timer(timer, final_time)

t1.clear()
t2.clear()
t3.clear()
t1.penup()
t1.goto(-100, 0)
t1.write(f'Game Over! Time: {final_time}s', font=('Arial', 16, 'bold'))
t2.hideturtle()
t3.hideturtle()
t1.hideturtle()

exitonclick()