import turtle
s=turtle.Turtle()
s.shape("turtle")
s.speed(100)
for i in range(10):
    s.circle(1000)
    s.circle(1050)
    s.circle(1100)
    s.circle(1150)
    s.circle(1200)
    s.right(5000)
turtle.mainloop()