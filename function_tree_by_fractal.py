from turtle import Turtle

def tree(plist, l, a, f):
    """plist is list of pens
    l is length of branch
    a is half of the angle between 2 branches
    f is factor by which branch is shortened
    from level to level"""
    if l > 5:
        lst = []
        for p in plist:
            p.forward(l)
            q = p.clone()
            p.left(a)
            q.right(a)
            lst.append(p)
            lst.append(q)
        tree(lst, l * f, a, f)


def main(x,y):
    p = Turtle()
    p.color("green")
    p.pensize(5)
    p.hideturtle()
    p.speed(4)
    ##make turtle invisible
#    p.getscreen().tracer(1,0)
    ##Return the TurtleScreen object the turtle is drawing
    p.left(90)
    p.penup()
    p.goto(x,y)
    p.pendown()
    t = tree([p], 110, 65, 0.6375)

main(0,-100)

