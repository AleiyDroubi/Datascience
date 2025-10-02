import turtle
import math

def draw_spirograph(radius1, radius2, angle):
  turtle.speed(0)
  turtle.penup()
  turtle.goto(0, radius1)
  turtle.pendown()
  for i in range(360):
    x = radius1 * math.cos(i * math.pi / 180) + radius2 * math.cos((i * angle) * math.pi / 180)
    y = radius1 * math.sin(i * math.pi / 180) + radius2 * math.sin((i * angle) * math.pi / 180)
    turtle.goto(x, y)

draw_spirograph(100, 50 , 25)
