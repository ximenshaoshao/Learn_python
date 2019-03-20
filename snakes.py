import turtle

def drawSnake(rad, angle, len, neckrad):
    for i in range(len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1, 180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1400, 800, 0, 0) ##启动窗口参数
    pythonsize = 30
    turtle.pensize(pythonsize)  ##运行轨迹宽度
    turtle.pencolor("blue")  ##运行轨迹颜色
    turtle.seth(-40) ##初始角度值
    drawSnake(40,90,5,pythonsize/2)

main()