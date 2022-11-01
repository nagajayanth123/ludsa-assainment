# Write a Program to find area of a circle using Function, take input from the user

import math


def area_of_the_circle(Radius):
    area = Radius ** 2 * math.pi
    return area


Radius = float(input("Please enter the radius of the given circle: "))
print(" The area of the given circle is: ", area_of_the_circle(Radius))
