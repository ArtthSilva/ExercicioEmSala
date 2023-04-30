VET = []
posicoes = []


for i in range(10):
    num = int(input("Digite um número: "))
    VET.append(num)


for i in range(len(VET)):
    for j in range(i+1, len(VET)):
        if VET[i] == VET[j] and VET[i] not in posicoes:
            posicoes.append(i)
            posicoes.append(j)


if len(posicoes) > 0:
    print("Os números repetidos foram estão nas posições:")
    for pos in posicoes:
        print(pos)
else:
    print("Não existe números repetidos no vetor.")
