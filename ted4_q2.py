valor = 1.3

qnt = int(input("quanto você quer comprar? "))

if qnt < 12:
  result = qnt * valor
  print(f'valor da compra: {result}')
else:
    valor = 1.0
    result = qnt * valor
    print(f'valor da compra: {result}')