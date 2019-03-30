##word statistic
'''
1输入英文文章
2 建立用于词频计算的空字典
3对文本的每一行计算词频
4从字典中获取数据对到列表中
5对列表中的数据排序
6输出结果
7turtle绘制结果
'''
import turtle

count = 10 ##top x words
data = []
word = []
yScale = 6
xScale = 30

def drawLine(t, x1, y1, x2, y2):
    t.penup()
    t.goto (x1, y1)
    t.pendown()
    t.goto (x2, y2)

def drawText(t, x, y, text):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.write(text)

def drawGraph(t):
    drawLine(t, 0, 0, 360, 0)
    drawLine(t, 0, 300, 0, 0)
    for x in range(count):
        x = x + 1
        drawText(t, x*xScale-4, -20, (word[x-1]))
        drawText(t, x*xScale-4, data[x-1]*yScale+10, data[x-1])

def drawRect(t, x, y):
    x= x*xScale
    y= y*yScale
    drawLine(t, x - 5, 0, x - 5, y)
    drawLine(t, x - 5, y, x + 5, y)
    drawLine(t, x + 5, y, x + 5, 0)
    drawLine(t, x + 5, 0, x - 5, 0)

def drawBar(t):
    for i in range(count):
        drawRect(t, i + 1, data[i])

####graph end####

def replacePunctuations(line):
    for ch in line:
        if ch in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
            line = line.replace(ch,"")
    return line

def processLine(line, wordCounts):
    #repalce punctuations with space
    line = replacePunctuations(line)
    words = line.split()
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1

def main():
    filename = input("Enter a filename:").strip()
    infile = open(filename, "r")
    wordCounts = {}
    for line in infile:
        processLine(line.lower(), wordCounts)

    pairs = list(wordCounts.items())
    items = [[x,y]for (y,x)in pairs]
    items.sort()
    for i in range(len(items)-1, len(items)-count-1, -1):
        print(items[i][1]+"\t"+str(items[i][0]))
        data.append(items[i][0])
        word.append(items[i][1])

    turtle.title("词频统计柱状图")
    turtle.setup(900, 750, 20, 20)
    t = turtle.Turtle()
    t.hideturtle()
    t.width(3)
    drawGraph(t)
    drawBar(t)
    turtle.done()

if __name__ == '__main__':
    main()