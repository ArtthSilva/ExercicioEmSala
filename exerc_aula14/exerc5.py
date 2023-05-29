letraRecebida = input("informe a letra")

def encontra_palavras(lista_palavras, letra):
    palavras_iniciadas_com_letra = []
    for palavra in lista_palavras:
        if palavra.startswith(letra):
            palavras_iniciadas_com_letra.append(palavra)
    return palavras_iniciadas_com_letra

lista = ["arthur", "michel", "anderson", "dart", "java", "messias"]
letra_inicial = letraRecebida

resultado = encontra_palavras(lista, letra_inicial)


print(resultado)