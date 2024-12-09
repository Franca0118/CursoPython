

# meuArray = [ 1 , 2, 3, 4]
# print(meuArray)
# del meuArray[2] # remove o 3 

# print(meuArray)
# meuArray.insert( 0 , "Valor a primeira casa")
# meuArray.insert( 1 , "Valor a segunda casa")
# print(meuArray)

# listaa = [1,2,3]
# listab = [4,5,6]
# listaa.extend(listab) # Junta as listas
# print(listaa)


lista_a = [1,2,3]
lista_b = lista_a.copy()
lista_a.append(2) # append igual ao js
print(lista_a, "//" , lista_b)



lista_atividade = ['joao', 'joaov','joaob']
for i in range(len(lista_atividade)):
    print(i,  ": ", lista_atividade[i] , sep="")


# As variaveis pegam os valores do array var1 = 3 ; var2 = 2
var1, var2 = [3,2]
print(var1 + var2)

# com o * ele o restante vira um array com o restante do array, e o var1 com o indice 0
var1, *restante = [2,3,5]
print(var1,'//', restante)
