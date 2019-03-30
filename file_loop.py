def main():
    fileName = input("Which file are the numbers in? ")
    infile = open(fileName, "r")
    sum = 0
    count = 0
    for line in infile:
        sum = sum + eval(line)
        count = count + 1
    print("\nThe average of the numbers is", sum / count)
main()

##or
def main2():
    fileName = input("Which file are the numbers in? ")
    infile = open(fileName, "r")
    sum = 0.0
    count = 0
    line = infile.readline()
    while line !="":
        sum = sum + eval(line)
        count = count + 1
        line = infile.readline()
    print("\nThe average of the numbers is", sum / count)
main2()