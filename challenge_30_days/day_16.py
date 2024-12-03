'''
    Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2). 
'''

from math import sqrt
import re

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def calc_dist(point1, point2):
    return sqrt((point2.x - point1.x)**2 + (point2.y - point1.y)**2)

def create_point_from_coordinates(coordinates):
    removed_commas = re.sub(",", " ", coordinates)
    coordinates_lst = removed_commas.split()
    x = coordinates_lst[0]
    y = coordinates_lst[1]
    return Point(int(x), int(y))    

point1_coordinates = input("Enter point 1 (just integers and splited by a comma and space) :")
point2_coordinates = input("Enter point 2 (just integers and splited by a comma and space) :")

point1 = create_point_from_coordinates(point1_coordinates)
point2 = create_point_from_coordinates(point2_coordinates)
print(calc_dist(point1, point2))