from turtle import *

speed(0)

def draw_cloud(x, y, size, color_name):
    penup()
    goto(x, y)
    pendown()
    color(color_name)

    # Erster Kreis links
    begin_fill()
    circle(size)
    end_fill()

    # Zweiter Kreis in der Mitte
    penup()
    goto(x + size * 1.5, y)
    pendown()
    begin_fill()
    circle(size)  #
    end_fill()

    # Dritter Kreis rechts
    penup()
    goto(x + size * 3, y)
    pendown()
    begin_fill()
    circle(size)
    end_fill()

    # Vierter Kreis über dem in der Mitte
    penup()
    goto(x + size * 1.5, y + size)
    pendown()
    begin_fill()
    circle(size)
    end_fill()

    penup()

def draw_sun(x, y, strahlen):
    penup()
    goto(x, y)
    color("orange")
    pendown()
    for i in range(strahlen):
        forward(150)
        right(180)
        forward(150)
        right(180)
        right(360 / strahlen)

def draw_sea():
    penup()
    goto(-400, -300)
    pendown()
    color("blue")
    begin_fill()
    forward(800)
    right(90)
    forward(600)
    right(90)
    forward(800)
    right(90)
    forward(600)
    end_fill()

