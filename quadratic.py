import math
def main():
    print("Let us finds the solutions to a quadratic\n")
    a, b, c = eval(input("Do enter the coefficents (a, b, c) in (ax*x + bx + c): "))
    delta = b*b - 4 *a *c
    if a == 0:
        x = -b/c
        print("\nThere is an solution",x)
    elif delta < 0:
        print("\nThe equation has no real roots!")
    elif delta == 0:
        x = -b / (2*a)
        print("\nThere is a double root at", x)
    else:
        discRoot = math.sqrt(delta)
        x1 = (-b + discRoot) / (2 * a)
        x2 = (-b - discRoot) / (2 * a)
        print("\nThe solutions are:" ,x1, x2)
main()