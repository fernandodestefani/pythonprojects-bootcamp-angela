import turtle
from turtle import Turtle, Screen
import random

# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

color_list = [(200, 10, 35), (247, 236, 37), (240, 244, 251), (239, 231, 3), (36, 216, 77), (223, 159, 61),
             (39, 79, 185), (28, 39, 159), (210, 73, 16), (17, 151, 18), (239, 39, 152), (65, 9, 27), (188, 14, 9),
             (216, 25, 127), (218, 140, 198), (223, 161, 7), (59, 12, 7), (67, 202, 227), (10, 96, 60), (84, 80, 212),
             (17, 19, 52), (237, 157, 218), (106, 232, 195), (99, 205, 136), (212, 84, 58), (8, 222, 235),
             (236, 171, 161)]


tim = Turtle()
turtle.colormode(255)
screen = Screen()
screen.title('Hirst Painting')
tim.penup()
tim.goto(-230, -200)
y = -200
for i in range(10):
   for c in range(10):
       tim.dot(20, random.choice(color_list))
       tim.forward(50)
   y += 50
   tim.goto(-230, y)

screen.exitonclick()
