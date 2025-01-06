sete = {1,3,3,3,3,3,3,3,3,3,3,3,3,3,3}
# set elimina valores duplicados 
print(sete)



array = [1,2,3,3,3,3,3,3,3,3]
# situacao: quero remover os valores duplicados de um array
arraylimpo = set(array)
print(arraylimpo)
# versao com for, sem usar o set
array2 = [1,2,3,3,3]
l = []
for i in array2:
    if i not in l:
        l.append(i)
        print(l)
array2 = l
print("A",array2)


a = set("Joao")
# o set nao garantem a ordem
print(a)