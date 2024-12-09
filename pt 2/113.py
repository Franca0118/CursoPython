def mult(*args):
    resu = 1.00
    if type(args[0]) == tuple:
        args = list(args[0])
    else:
        args = list(args)

    for i,b in enumerate(args):
        try:
            float(b)
            print(f"{b} * {resu} = {resu * float(b)}")
            resu *= float(b)
        except:
            print(f"{b} não é um numero")
            
    return resu

def parim(a):
        try:
            float(a)
            return f"{a} PAR" if a%2 == 0 else f"{a} IMPAR"
        except:
            return f"{a} NAO É UM NUMERO"
            
    
print(mult(2,4,"a",3))
print('---')
print(parim(2))
print(parim(3))
print(parim("A"))