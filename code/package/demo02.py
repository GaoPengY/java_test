import turtle
#获取画笔
t = turtle.Pen()
#设置背景颜色
turtle.bgcolor("black")
#将要绘制的多边形的边数
sides = 6
#将要使用的颜色列表
colors = ["yellow","purple","red","pink","blue","orange"]

for i in range(360):
    #设置画笔的颜色
    t.pencolor(colors[i%sides])
    #画笔的移动轨迹
    t.forward(i*3/sides + i)
    #转动的角度
    t.left(360/sides + 1)
    #画笔的宽度
    t.width(i*sides/180)
    t.left(92)
else:
    print("******end***********")