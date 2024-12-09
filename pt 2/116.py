def a(a,b):
    def c():
        return f"{a} {b}"
    return c()

r = a('ola','mundo')
print(r)        

# def a(a,b):
#     def c():
#         return f"{a} {b}"
#     return c

# r = a('ola','mundo')
# print(r())    
        

def sand(a):
    def nome(b):
        return f"ola {b}, {a}"
    return nome


y = sand("Boa noite")
i = sand("Boa tarde")
print(y("joao"))
print(i("maria"))