#高阶函数
#变量可以指向函数
foo=abs
print(foo(-199))
#函数名也是变量
#abs=10
#print(abs(10))
#注：由于abs函数实际上是定义在import builtins模块中，所以要修改abs变量的指向在其他模块也生效
#要用 import builtins;builtins.abs=10

#传入函数
#既然变量可以指向函数，函数的参数能接受变量，那么一个函数就可以接受另一个函数作为参数，
#这种函数就称之为高阶函数
def add(x,y,f):
    return f(x)+f(y)
print(add(-100,-200,abs))
