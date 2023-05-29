num = int(input("fatorial de: "))
def calcula_fatoral(num):
    if num < 0:
        raise ValueError('O número deve ser não-negativo')
    elif num == 0 or num == 1:
        return 1
    else:
        fatorial = num
        while num > 1:
            num -= 1
            fatorial *= num
        return fatorial

print(calcula_fatoral(num))