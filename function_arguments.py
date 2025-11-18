#位置参数
#
def my_pow(x,n=2):
    s=1
    while n>0:
        s*=x
        n-=1
    return s
def add_end(l=None):
    if l is None:
        l = []
    l.append('end')
    return l

def calc(number):
    sum = 0
    for n in number:
        sum+=n
    return sum
#可变参数
#可变参数接收到的是一个tuple  ()
def calc_variable_arguments(*numbers):
    sum = 0
    for n in numbers:
        sum+=n
    return sum
nums = [1,2,3,4]

calc_variable_arguments(1,2,3,4)
calc_variable_arguments(nums[0],nums[1],nums[2],nums[3])
calc_variable_arguments(*nums)
#关键字参数
#关键字参数允许你传入0个或者任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict  {'key':'value'}
def person(name,age,**other):
    print('name:',name,'age:',age,'other',other)
person('Bessie',30,gender='female',height=152)
others = {'gender':'female','height':152}
person('Bessie',30,**others)
#**others表示把extra这个dict的所有key_value用关键字参数传入函数的**other参数，other将获得一个dict,
# 注意这个other获得的dict是others的一份拷贝，对other的改动不会影响倒函数外的others
#命名关键字参数
#命名关键字需要一个特殊分隔符 * ， * 后面的参数被视为命名关键字参数
def person_1(name,age,*,city,job):
  print(name,age,city,job)
person_1('Jack',24,city='Beijing',job='Engineer')
#如果定义了一个可变参数，后面跟着的命名关键字参数就不需要一个特殊分隔符 * 了
def person_2(name,age,*args,city,job):
    print(name,age,args,city,job)

def mul(a,*args):
    sum=a
    for n in args:
        sum *=n
    return sum
