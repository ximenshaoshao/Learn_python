import math

def square(x):
    return x * x
def distance (x1, y1, x2, y2):
    dist = math.sqrt(square(x1-x2) + square(y1 - y2))
    return dist
def isTriangle(x1, y1, x2, y2, x3, y3):
    flag = ((x1 - y1) * (y3 - y2)-(x3 - x2) * (y1 - y2)) != 0 ##共线
    return flag
def main():
    print("Please enter (x,y) of the points and continue: ")
    x1, y1 = eval(input("Point1: (x,y) = "))
    x2, y2 = eval(input("Point2: (x,y) = "))
    x3, y3 = eval(input("Point3: (x,y) = "))
    if(isTriangle(x1, y1, x2, y2, x3, y3)):
        perim = distance(x1, y1, x2, y2)
        + distance(x3, y3, x2, y2)
        + distance(x3, y3, x1, y1)
        print("The perimeter of the triangle is: {0:0.2f}".format(perim))
    else:
        print("It's NOT a triangle, they are on the same line!")
main()