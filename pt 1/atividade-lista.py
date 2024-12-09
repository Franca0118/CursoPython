import os
listadeCompras = []

while True:
    os.system('clear')
    print("- LISTA DE COMRPAS -")
    print("- ESSA É SUA LISTA DE COMPRAS -")
    for i, item in enumerate(listadeCompras,start=1):
        print(f"/ {i} -> {item} \ ")
    print(" ")
    print("- 0 para sair")
    print("- 1 para adicionar")
    print("- 2 para remover")
    resp = input("o que deseja fazer?")
    
    if resp == '0':
        break
    elif resp == '1':
        listadeCompras.append(input("Qual produto deseja adicionar? : "))
    elif resp == '2':
        resp2 = input("nome ou numero do produto")
        try:
            listadeCompras.pop(int(resp2)-1)
        except:
            try:
                listadeCompras.remove(resp2)
            except:
                print("Nao tem esse produto")    
    
        
        

