import math

def main():
    print("This program is used for find real solution of a quadratic equation.\n")
    try:
        a, b, c = eval(input("Please enter the coefficients a, b, c of (ax2 + bx + c):"))
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\nThe solutions are:", root1, root2)
    except ValueError as excObj:
        if str(excObj) == "math domain error":
            print("No real Roots.")
        else:
            print("You didn't give me the right number of coefficients. Please correct!")
    except NameError:
        print("\nYou didn't enter three numbers.")
    except TypeError:
        print("\nYour inputs were not all numbers")
    except SyntaxError:
        print("\nYour inputs was not in the correct form. Missing comma?")
    except:
        print("\nSomething wrong, Please check and try again")
main()