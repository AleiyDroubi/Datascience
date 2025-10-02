import turtle

def draw_spiral(angle, step):
  while True:
    turtle.forward(step)
    turtle.left(angle)
    step += 1

turtle.speed(0)
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
draw_spiral(40, 1)
turtle.hideturtle()
