lista1 = []
i = 0
print("Dati un numar (pentru a termina citirea, apasati ~Enter~): ")
while True:             
    i += 1
    inp = input(":")  
    if inp != "":
        lista1.append(int(inp))
    if inp == "":       
        break   
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
