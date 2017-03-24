#name = raw_input('please input your name')

def power(x, n=2):
    s = 1
    while n>0:
        n = n-1
        s *= x
    return s

def Log(str):
    total = power(4, 4)
    print total
    return

def fact(i):
    return fact_itr(i, 1)

def fact_itr(i, j):
    if(i==1):
        return j
    return fact_itr(i-1, i*j)
#列表生成器
def ListCreate(i):
    alist = [x*x for x in range(i) if x%2==0]
    return alist
#生成器
def Generate(i):
    g = (x * x for x in range(i))
    return g
#函数生成器
def fib(max):
    n, a, b = 0, 0, 1
    li = []
    while n < max:
        li.append(b)
        yield b
        a, b = b, a+b
        n = n+1

def addFun(x, y, fun):
    return fun(x)+fun(y)

def f(x, y):
    return x%y == 0

def not_prime(x):
    if x == 1:
        return False
    elif x== 2:
        return True
    else:
        sub = range(2, x-1)
        for i in sub:
            if f(x,i):
                return False
    return True

#print ListCreate(10)
#print Generate(10)
#print fib(10)
#print addFun(5,10, fact)
#print map(f,ListCreate(10))
print filter(not_prime, range(1, 100))