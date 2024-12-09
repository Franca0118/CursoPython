def printmsg(a):
    print(a)

def execFunc(f,a):
    f(a)

execFunc(printmsg, "ola")



def printmsg(a,b='a'):
    print("ola", a, b)

def execFunc(f,*args):
    f(*args)

execFunc(printmsg, "joao", 'victor')