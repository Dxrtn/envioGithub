def dividir(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Erro: Divisão por zero não é permitida."

num1 = (int(input("Digite o dividendo:")))
num2 = (int(input("Digite o divisor:")))

print(dividir(num1, num2))