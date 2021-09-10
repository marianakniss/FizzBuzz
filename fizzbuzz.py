print("Imprimindo números de 1 a 100")

for numero in range(1,101):
    if (numero % 3) == 0 and (numero % 5) == 0:
        print("BuzzFizz")    
    elif (numero % 3) == 0:
        print("Buzz")
    elif (numero % 5) == 0:
        print("Fizz")
    else:
        print(numero)