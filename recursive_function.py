#递归函数
#递归函数的优点是逻辑清晰，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰
import math


def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)

print(fact(10))
#尾递归
#尾递归指，在函数返回时，调用自身本身，并且，return语句不能包含表达式。
#这样，编译器或者解释器可以把尾递归做优化，使递归本身不论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况
#Python不支持尾递归优化
def fact_tall(n,a=1):
    if n==1:
        return a
    else:
        return fact_tall(n-1,a*n)
print(fact_tall(10))
#通过递归实现汉塔模型
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

move(5, 'A', 'B', 'C')
