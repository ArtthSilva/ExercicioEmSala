num = int(input("digite um numero: "))
 
if num > 1:

    for i in range(2, num):
 
        if (num % i) == 0:
            print(num, "nao é primo")
            break
    else:
        print(num, "é primo")
 
else:
    print(num, "nao é primo")