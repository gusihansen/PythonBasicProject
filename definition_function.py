import cmath
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>0:
        return x
    else:
        return x
#print(my_abs(-100))
def nop():
    pass

def root_finding_quadratic(x,y,z):
    x1= ((-y)+cmath.sqrt(y**2-4*x*z))/2*x
    x2 = ((-y)-cmath.sqrt(y**2-4*x*z))/2*x
    return x1,x2


