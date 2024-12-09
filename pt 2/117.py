def CriarMultiplicador(a):
    def Multiplicador(b):
        return a * b
    return Multiplicador

    
Duplica = CriarMultiplicador(2)
Triplica = CriarMultiplicador(3)
Quadriplica = CriarMultiplicador(4)
print(Duplica(3))
print(Triplica(3))
print(Quadriplica(3))
