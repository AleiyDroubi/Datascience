import turtle


def draw_branch(length, angle):
  if length > 5:
    turtle.forward(length)
    turtle.left(angle)
    draw_branch(length * 0.7, angle)
    turtle.right(2 * angle)
    draw_branch(length * 0.7, angle)
    turtle.left(angle)
    turtle.backward(length)
turtle.bgcolor("light blue")
turtle.color("green")
turtle.speed(0)
turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()
draw_branch(100, 30)
turtle.hideturtle()
