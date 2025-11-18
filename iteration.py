#迭代iteration
#list迭代
import math

l=['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
for n in l:
    print(n)
t=(1,2,3,4,5,6,7,8,9)
#tuple迭代
for n in t:
    print(n)
d = {'a': 1, 'b': 2, 'c': 2}
#dic的key迭代 无序
for key in d:
    print(key)
# dic的value迭代 无序
for value in d.values():
    print(value)

#字符串迭代
str = 'hello,world'
for ch in str:
    print(ch)
#判断是否可以迭代
from collections.abc import Iterable
print(isinstance(str,Iterable))
print(isinstance(d,Iterable))
print(isinstance(l,Iterable))
print(isinstance(t,Iterable))

#对list实现类似java的索引下标循环，使用Python内置的enumerate函数，将list变成索引元素对。
for i,value in enumerate(l):
    print(i,":",value)
#for循环同时引入两个变量
for x,y in [(1,2),(2,3),(3,4),(5,6)]:
    print(x,y)




def find_min_and_max(l):
    if l==[]:
        return None,None
    temp_max_value = l[0]
    temp_min_value = l[0]
    for i in l:
        if i>temp_max_value:
            temp_max_value = i
        elif i<temp_min_value:
            temp_min_value = i

    return temp_min_value,temp_max_value
if find_min_and_max([]) != (None, None):
    print('测试失败!')
elif find_min_and_max([7]) != (7, 7):
    print('测试失败!')
elif find_min_and_max([7, 1]) != (1, 7):
    print('测试失败!')
elif find_min_and_max([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')