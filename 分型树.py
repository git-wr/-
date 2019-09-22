# -*- coding: utf-8 -*-
"""
绘制分型树
"""
import turtle as t1
def draw_smalltree(tree_length,tree_angle):
    """
    绘制分型树函数
    """
    if tree_length >= 3:
        t1.forward(tree_length) #往前画
        t1.right(tree_angle) #往右转
        draw_smalltree(tree_length -10,tree_angle) #画下一支，直到画到树枝长小于3

        t1.left(2 * tree_angle) #转向画左
        draw_smalltree(tree_length -10,tree_angle) #直到画到树枝长小于3

        t1.rt(tree_angle) #转到正向上的方向，然后回溯到上一层
        if tree_length <= 30: #树枝长小于30，可以当做树叶了，树叶部分为绿色
            t1.pencolor('green')
        if tree_length > 30:
            t1.pencolor('brown')  #树干部分为棕色
        t1.backward(tree_length) #往回画，回溯到上一层

def main():
    t1.penup()
    #t1.pencolor('green')
    t1.left(90) #因为树是往上的，所以先把方向转左
    t1.backward(250) #把起点放到底部
    t1.pendown()
    tree_length=100 #设置的最长树干为100
    tree_angle=20   #树枝分叉角度，设置为20
    draw_smalltree(tree_length,tree_angle)
    t1.exitonclick() #点击才关闭画画窗口
if __name__ == '__main__':
    main()