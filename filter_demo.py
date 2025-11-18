#过滤器
#Python内建的filter()函数用于过滤序列
#和map类似，filter()也接收一个函数，一个序列，不同的是，filter()把传入的函数依次作用于每个元素，
#根据返回值是True还是False决定保留还是丢弃元素，函数返回值为Iterator

#在一个list中，删除掉偶数，只保留奇数
def foo_1(l):
    return list(filter(lambda x: x%2==1,l))

print(foo_1([1, 2, 4, 5, 6, 9, 10, 15]))

#把一个序列中的空字符串删除掉
def foo_2(l):
    return list(filter(lambda s: s and s.strip(),l))
print(foo_2(['A', '', 'B', None, 'C', '  ']))


#获取100以内的所有素数
def foo_3():
    n1=1
    while True:
        n1=2+n1
        yield n1
def foo_filter(n):
    return lambda x:x%n>0
def foo_4():
    yield 2
    g=foo_3()
    while True:
        n2 = next(g)
        yield n2
        g = filter(foo_filter(n2) ,g)

# for n in foo_4():
#     if n<100:
#         print(n)
#     else:
#         break
#筛选回数，回数是指从左往右和从右往左读都是一样的数

def str_reverse(n):
    s=str(n)
    return s==s[::-1]
def filter_practice():
    l = list(range(100))
    l1 = list(filter(str_reverse,l))
    print(l1)
filter_practice()