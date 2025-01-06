
def executar(funcao, *args):
    return funcao(*args)

def multiplica(mult):
    def multiplicar(numero):
        return mult * numero
    return multiplicar
print(multiplica(2)(5))

print(executar(lambda x,y:x+y,2,7))

# o 3 esta como parametro n
func = executar(lambda n: lambda m: n * m, 3)
print(func(2))