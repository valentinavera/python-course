# listas
lista = list()
lista = []
fibonacci = [0, 1, 1, 2, 3, 5]
print(fibonacci)
print(fibonacci[4])
print(fibonacci[-1])

sublista = fibonacci[2 : 4]
print(sublista)

fibonacci = fibonacci + sublista
print(fibonacci)

fibonacci[6] = 8
fibonacci[7] = 13
print(fibonacci)

fibonacci.append(8 + 13)
print(fibonacci)

fibonacci.append("A")
fibonacci.append(["A", "B"])
print(fibonacci)

print(len(fibonacci))
print(fibonacci[10][0])
