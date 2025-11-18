#列表生成式
l= list(range(11,16))
print(l)
#生成[1x1,2x2,3x3...,10x10]的list
l=[]
for x in range(1,11):
    l.append(x * x)

#Python写法
l=[x * x for x in range(1,11)]
#筛选出偶数
l=[x * x for x in range(1,11) if x%2 ==0]
#两层循环
l=[m + n for n in 'abc' for m in 'emd']
#列出c盘下文件名
import os
l=[d for d in os.listdir('c:')]
#for循环同时使用两个甚至更多的变量，比如dict的item()可以同时迭代key和value
d={'x': 'A', 'y': 'B', 'z': 'C' }
for key,value in d.items():
    print(key,'=',value)
print([key+'='+value for key,value in d.items()])

#大写变小写
print([key.lower() +'='+value.lower() for key,value in d.items()])

#列表生成的if...else用法
#if在for之前代表表达式，需要跟上else
l=[x*x if x%2==0 else None for x in range(1,11)]
#if在for之后代表筛选条件，不能带上else
l=[x*x for x in range(1,11) if x%2==0]


def to_lower(l):
    return [x.lower()  for x in l if isinstance(x,str)]

print(to_lower(['Hello', 'World', 18, 'Apple', None]))