lista = [
    {'nome':'a','time':'h'},
    {'nome':'b','time':'j'},
    {'nome':'f','time':'i'},
    {'nome':'d','time':'t'},
    {'nome':'c','time':'y'},
    {'nome':'e','time':'q'}
]


def orden(item):
    print(item)
    return item['nome']

lista.sort(key=orden)
print("--------")
for i in lista:
    print(i)

print("--------2---------")
# a define cada item, podendo receber qualquer nome
lista.sort(key=lambda a:a['nome'])
print("--------")
for i in lista:
    print(i)
lista.sort(key=lambda a:a['time'])
print("--------")
for i in lista:
    print(i)