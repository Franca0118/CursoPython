# apos parametros com valores padrao, os seguintes precisam de possuir o valor padrao
def soma2(a,b,c=None, d):
    if c is not None:
        print(a + b + c)   
    else:
        print(a + b) 

soma2(1,2)
soma2(b=2,a=1)