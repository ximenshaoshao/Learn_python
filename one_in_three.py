##to find the biggest number in three numbers
import math
def main():
    x1, x2, x3 = eval(input("Please enter three random number, seperated by comma, e.g. 1,2,3:"))
    max = x1
    if x2 > max:
        max = x2
    elif x3 > max:
        max = x3
    print("The largest number is:", max)