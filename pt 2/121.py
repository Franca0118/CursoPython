

import copy
a = {
    "a" : 1,
    "b" : 2
}
b = a

# A é alterado
b["a"] = 3
print(a)

# ----------------------
print("------")

a = {
    "a" : 1,
    "b" : 2,
    "c" : [1,2,3]
}
c = a.copy()
c["c"][2] = "MBAPPE"
# O A TAMBEM É ALTERADO, SENDO O PROBLEMA DO COPY
print("A", a)
print("C", c)

print("------")
a = {
    "a" : 1,
    "b" : 2,
    "c" : [1,2,3]
}
c = copy.deepcopy(a)
c["c"][2] = "MBAPPE"
print("A", a)
print("C", c)

