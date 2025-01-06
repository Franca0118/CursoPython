# meuarray = []
# while True:
#     meuarray.append(input("Digite algo"))
#     print(meuarray.count("a"))



letra = "j"
meuset = set()
while True:
    meuset.add(input("Digite uma letra").lower())

    if letra in meuset:
        break