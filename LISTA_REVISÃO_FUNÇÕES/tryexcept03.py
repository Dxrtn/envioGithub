try:
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    opt = input("Digite uma operação(+  -  *  /): ")
    match opt:
        case '+':
            print(num1 + num2)
        case '-':
            print(num1 - num2)
        case '*':
            print(num1 * num2)
        case '/':
            print(num1 / num2)
except ValueError:
    print("Você deve digitar um número inteiro")
except ZeroDivisionError:
    print("Não existe divisão por 0")