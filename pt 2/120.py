a = {
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5,
    "f":6,
    "g":7,
    "h":8,
    "i":9
}


print(len(a))
print(a.__len__())
print(a['a'])
soma = 0
for i in a:
    print(i)
    soma += a[i]
print(soma)

print(a.keys())

for i in a.keys():
    print(a)
for i in a.values():
    print(i)
for i,a in a.items():
    print(i,a)





a.setdefault("j", 10)
print(a['j'])


