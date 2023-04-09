convidados = ["Vinícius Júnior", "Neymar", "Zico", "Djonga", "LeBron James"]
for convidado in convidados:
    print('Eai',convidado, "você está convidado para um jantar em minha casa!")
    print()
print('O',convidados[4], "não poderá comparecer!")
print()

ultima_lista = convidados[4] = "Casimiro"
print('A nova lista de convidados é', convidados)
for convidado in convidados:
    print ('Eai', convidado, "você está convidado para um jantar em minha casa!")