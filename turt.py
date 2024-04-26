import turtle
s=turtle.Turtle()
turtle.bgcolor("black")
s.color("white")
s.shape("turtle")
s.speed(0)
for i in range(300):
    s.circle(i)
    s.right(5)
turtle.mainloop()