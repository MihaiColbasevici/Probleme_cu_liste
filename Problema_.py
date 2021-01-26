prenume = ['Mihai', 'George', 'Ana', 'Dan', 'Ion', 'Geta', 'Vio']
varsta = [14, 23, 15, 14, 12, 41, 39]
# a)
i = 0
for i in range(0, 6):
    print(prenume[i], 'are varsta de', varsta[i])

# b)
prenume.append('Andreea')
prenume.append('Ioan')
varsta.append(34)
varsta.append(23)
print(prenume)
print(varsta)

# c)
del prenume[2]
del varsta[2]

# d)
print(prenume[0:3])

# e)
print(prenume[::-1])

# f)
print(prenume[2:4], '\t', varsta[2:4])
print(prenume[0:5], '\t', varsta[0:5])