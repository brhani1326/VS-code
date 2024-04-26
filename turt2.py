import turtle
import colorsys
s=turtle.Turtle()
turtle.bgcolor("black")
h=0.0
for i in range(10):
    s.color(colorsys.hsv_to_rgb(h,1,1))
    s.square(100)
    s.right(36)
    h+=0.1
turtle.mainloop()