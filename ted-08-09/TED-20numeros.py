
numeros = []

for i in range(20):
    numero = int(input(f"{i} número: "))
    numeros.append(numero)

print("Os números lidos em ordem inversa são:")
for i in range(19, -1, -1):
    print(numeros[i])
