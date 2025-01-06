a = {
    "nome": 1 ,
    "sobrenome": 2
}
nome = a.pop("nome") # Pega o valor e deleta
print("POP",nome,a)



a = {
    "nome": 1 ,
    "sobrenome": 2
}
ultima = a.popitem() # remove a ultima chave
print("POP ITEM",ultima, a)
a = {
    "nome": 1 ,
    "sobrenome": 2
}

a.update({

})
print("UPDATE",a) # VAZIO ELE NAO FAZ "NADA"


a = {
    "nome": 1 ,
    "sobrenome": 2
}
a.update({
    "nome":"Joao",
    "sobrenome": "Victor",
    "idade":18
})
print("UPDATE2",a)

a = {
    "nome": 1 ,
    "sobrenome": 2
}
tupla = (("nome", "Kilian"),("sobrenome", "Mbappe"),("idade", 18))
a.update(tupla)
print("UPDATE3",a)


