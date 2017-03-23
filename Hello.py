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
Log("hello world")