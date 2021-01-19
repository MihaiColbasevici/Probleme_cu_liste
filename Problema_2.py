with open("input.txt", 'w') as f:
    f.write(input("Dati elementele (separate prin 'spatiu'): "))
with open("input.txt", 'r') as k:
    var = k.read()
lista1 = var.split()
for i in range(len(lista1)):
    lista1[i] = int(lista1[i])
# a)
print (*lista1)

# b)
lista2 = sorted(lista1)
print("Oridnea crescatoare: ", lista2)

# c)
lista3 = lista2[::-1]
print("Ordinea descrescatoare: ", lista3)

# d)
print("Numarul de elemente: ", len(lista1))

# e)
print("Elementul maxim: ", max(lista1))

# f)
print("Elementul minim: ", min(lista1))

# g)
lista4 = lista1 + [-111]
print("Adaugam elementul '-111': ", lista4)

# h)
lista5 = lista1[:1] + [-222] + lista1[1:]
print(lista5)

