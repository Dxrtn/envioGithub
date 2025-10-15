try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    result = num1/num2
    print(result)
except ZeroDivisionError:
    print("não é possível dividir por zero")