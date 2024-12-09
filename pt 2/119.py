pessoa = {}
chave = "a"

pessoa[chave] = "Joao"
print(pessoa[chave])
pessoa[chave] = "Mbappe"
print(pessoa[chave])


pessoa = {'aa': 'neymar'}
print(pessoa.get("aa", "NAO TEM"))
pessoa = {}
print(pessoa.get("aa", "NAO TEM"))


del pessoa[chave]
print(pessoa[chave])
