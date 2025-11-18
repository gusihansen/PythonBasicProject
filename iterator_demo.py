#迭代器
#iterable 可以直接作用于for循环
from collections.abc import Iterable, Iterator
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
print(isinstance((),Iterable))
print(isinstance((x for x in range(10)),Iterable))
#iterator 可以被next() 函数不断调用并返回下一个值，直到抛出stopIteration
print(isinstance((x for x in range(10)),Iterator))
print(isinstance((),Iterator))
print(isinstance([],Iterator))
print(isinstance('12323',Iterator))

#集合数据类型如list,dict,str等是Iterable但不是Iterator,不过可以通过iter()函数获得一个Iterator对象
print(isinstance(iter([]),Iterator))