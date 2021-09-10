def f(n):
    if n == 1 or n == 2:
        return 1
    elif n == 0:
        return 2
    else:
        return f(n-1) + f(n-2)

resposta = f(6)
print(resposta)