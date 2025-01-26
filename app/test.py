from turtleforbeginners import *
from turtle import *
# Fenster initialisieren
screen = Screen()
screen.bgcolor("sky blue")
speed(0)
# Parameter der Wolke (x, y, größe, farbe)
meer()
sun(-200, 200, 20)
draw_cloud(-200, 100, 30, "white")
draw_cloud(0, 50, 20, "gray")
draw_cloud(200, -100, 40, "light gray")

hideturtle()
done()