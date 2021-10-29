# import colorgram
#
# colors = colorgram.extract("/Volumes/Extreme SSD/Python Bootcamp/Day 18/Mac/the_hirst_painting/image.jpg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)

import random
import turtle

screen = turtle.Screen()
screen.title("The Hirst Painting")


color_list = [(131, 166, 205), (222, 148, 106), (31, 42, 61), (199, 134, 147), (165, 59, 48), (140, 184, 162), (39, 105, 157), (238, 212, 89), (152, 58, 66), (217, 81, 70), (169, 29, 33), (236, 165, 156), (50, 112, 90), (35, 61, 55), (17, 97, 71), (156, 33, 30), (231, 160, 165), (53, 44, 49), (170, 188, 221), (57, 51, 48), (189, 100, 110), (31, 60, 109), (103, 127, 161), (34, 151, 209), (174, 200, 188), (65, 66, 56)]

x_initial = -200
y_initial = -200

turtle.colormode(255)
timmy = turtle.Turtle()
timmy.penup()
timmy.goto(x_initial, y_initial)

# print(timmy.xcor())

for _ in range(10):
    for _ in range(10):
        timmy.color(random.choice(color_list))
        timmy.dot(20)
        xcor = timmy.xcor() + 50
        timmy.setx(xcor)
        pass
    ycor = timmy.ycor() + 50
    timmy.setx(x_initial)
    timmy.sety(ycor)

screen.exitonclick()
