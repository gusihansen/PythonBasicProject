#map
#map接收两个参数，一个是函数，一个是Iterable,map将传入的函数作用于每个元素，并把结果作为新的Iterator返回。
from functools import reduce


def foo(x):
    return x*x
g=map(foo,[1,2,3,4,5,6,7,8,9])
print(list(g))
print(list(map(str,[1,2,3,4,5,6,7,8,9])))

#reduce
#reduce 把一个函数作用在一个序列[x1,x2,x3,x4,...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累计计算，
# 其效果就是 reduce(f,[x1,x2,x3,x4])=f(f(f(x1,x2),x3),x4)
def foo_1(x,y):
    return x+y
print(reduce(foo_1,[1,2,3,4,5,6,7]))

#字符串转int
def foo_2(x,y):
    return 10*x+y
def foo_3(x):
    d={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return d[x]
print(reduce(foo_2,list(map(foo_3,'1234567'))))

print(reduce(lambda x,y:10*x+y,map(foo_3,'12345644')))

#map 练习 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def foo_upper(s):
    l = [x.lower()  for x in s]
    l[0] = l[0].upper()
    l=reduce(lambda x,y:x+y,l)
    return str(l)
print(list(map(foo_upper,['adam', 'LISA', 'barT'])))

def prod(l):
    return reduce(lambda x,y:x*y,l)
print(prod([3,5,7,9]))

def foo_4(x,y):
    return 10*x+y
def foo_5(x,y):
    return 0.1*x+y

def foo_6(s):
    d={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':'.'}
    return d[s]

def foo_7(l):
    for index,value in enumerate(l):
        if value=='.':
            l[index]=0
            l1 = l[0:index]
            l=l[index:len(l)]
            #list.reverse(l)
            return l1,l[::-1]
        else:
            continue
    return l,[0]

def str2float(s):
    l = list(map(foo_6,s))
    l1,l2 = foo_7(l)
    return reduce(foo_4,l1)+reduce(foo_5,l2)
#list.reverse(l)
print(str2float('3.100'))
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')