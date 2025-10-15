valor = input("Digite um número: ")
try:
    numero = float(valor)
    print("Obrigado!")
except ValueError:
    print("Digite um valor válido!")