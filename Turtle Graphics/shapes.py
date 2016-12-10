from turtle import *
# from draw_a_square import *
# from draw_a_star import *
# from draw_a_circle import *
# from draw_a_hexagon import *
# from draw_a_octogon import *
# from draw_a_eqtri import *

def draw_square(size):
    for i in range(4):
        forward(size)
        left(90)

def draw_star():
    setheading(180)
    forward(150)
    right(120)
    forward(150)
    right(120)
    forward(150)
    up()
    setheading(90)
    forward(85)
    down()
    setheading(180)
    forward(150)
    left(120)
    forward(150)
    left(120)
    forward(150)

def draw_octogon():
    setheading(180)
    forward(100)
    right(45)
    forward(100)
    right(45)
    forward(100)
    right(45)
    forward(100)
    right(45)
    forward(100)
    right(45)
    forward(100)
    right(45)
    forward(100)
    right(45)
    forward(100)

def draw_hexagon():
    setheading(180)
    forward(100)
    right(72)
    forward(100)
    right(72)
    forward(100)
    right(72)
    forward(100)
    right(72)
    forward(100)

def draw_eqtri():
    setheading(180)
    forward(100)
    right(120)
    forward(100)
    right(120)
    forward(100)

def draw_circle(size):
    turtle.circle(size)

if __name__ == '__main__':
        draw_square()
        draw_eqtri()
        draw_hexagon()
        draw_circle()
        draw_octogon()
        draw_star()
        mainloop()
