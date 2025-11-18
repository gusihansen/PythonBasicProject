#切片
l=['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(l[0:3])
print(l[:3])
print(l[1:3])
#倒数切片
print(l[-2:-1])

l1=list(range(100))
#后10个数
print(l1[-10:])
#前11到20个数
print(l1[10:20])
#前11到20个数，每两个数取1个
print(l1[10:20:2])
#每11个数取1个
print(l1[::11])
#只写[:]可以原样复制一个list
print(l1[:])
#tuple切片，唯一区别是tuple不可变，因此tuple也可以用切片操作，知识操作结果仍然是tuple
t=(0,1,2,3,4,5,6,7,8,9)
print(t[:3])
#字符串切片
str='字符串切片'
print(str[:3])
print(str[-2:])
print(str[::2])
#切除末尾
print(str[0:-1])

def trim(s):
    while s[:1] ==' ':
       s=s[1:]
    while s[-1:] ==' ':
        s=s[0:-1]
    return s

print(trim(' hello world    '))
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')