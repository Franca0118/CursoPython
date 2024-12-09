# a, b, *r = 1,2,3,4,5
# print(a,b,r)

def soma(*args):
    args = list(args)
    soma = 0
    msg = ""
    if not args:
        msg = "voce nao passou argumentos"
        return msg
    for i,num in enumerate(args):
        soma += num
        if i == 0:
            msg += f"{num} "
        else:
            msg += f"+ {num} "


    return f"{msg}= {soma}"


print(soma(1,2,3,4,5,5,6))
print(soma(2))
