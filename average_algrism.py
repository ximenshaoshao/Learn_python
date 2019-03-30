###Yes no count
def main():
    sum = 0.0
    count = 0
    moredata = "yes"
    while moredata[0] in ["y","Y"]:
        x = eval(input("Enter a number >> "))
        sum = sum + x
        count = count + 1
        moredata = input("Do you have more numbers (yes or no)?")
    print("\nThe average of the number is", sum/count)
#main()

###beacon loop
##condition equals to beacon,quit loop
def main2():
    sum = 0.0
    count = 0
    xStr = input("Enter a number (<Enter> to quit)>>")
    while xStr != "":
        x = eval(xStr)
        sum = sum + x
        count = count + 1
        xStr = input("Enter a number(<Enter> to quit)>>")
    print("\nThe average of the numbers is", sum / count)
main2()