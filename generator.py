#生成器
#生成器可以节省存储空间

l=[x*x for x in range(10)]
#把列表的声生成式的[]改成(),就创建了一个generator
g=(x*x for x in range(10))
print(g)
# <generator object <genexpr> at 0x00000211B0F19150>
#next(g)可以获取元素
print(next(g))
#注意不能越界
#一般不使用next(generator)来获取元素
for n in g:
    print(n)

def fib(n):
    t ,a ,b =0,0,1
    while t<n:
        print(b)
        a,b = b, a+b
        t+=1
fib(10)

# 注意a,b = b,a+b  等效于 t=(b,a+b), a=t[0] ,b=t[1]
#将print(b)修改为yield b,函数变为generator函数
def fib_generator(n):
    t ,a ,b =0,0,1
    while t<n:
        yield b
        a,b = b, a+b
        t+=1

g = fib_generator(9)
print(g)
#<generator object fib_generator at 0x0000016F92E3D1C0>
for b in g:
    print(b)
#普通函数式顺序执行，遇到return语句就返回，
# 而generator函数在每次调用next()的时候执行，遇到yield语句返回，再次执行从yield处继续执行

#验证
def generator_demo1():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3
    print('step 4')
    yield 4
    print('step 5')
    yield 5
    print('step 6')
    yield 6
#调用generator函数会生成一个generator对象，多次调用generator函数会创建多个相互独立的generator

# >>> next(generator_demo1())
# step 1
# 1
# >>> next(generator_demo1())
# step 1
# 1
# >>> next(generator_demo1())
# step 1
# 1
def yang_hui():
    l=[1]
    l1=[]
    a=0
    while True:
        #print(l)
        yield l
        l1 = l
        length = len(l1)
        index = 1
        l=[1]
        while index<=length:
            if length>index:
                l.append(l1[index-1]+l1[index])
            else:
                l.append(1)
            index +=1
        a+=1
