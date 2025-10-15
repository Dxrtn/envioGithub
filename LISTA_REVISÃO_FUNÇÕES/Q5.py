def calc_imc(height, weight):
    imc = (weight/(height*height))
    return imc

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
indice = calc_imc(altura, peso)
print(f"Seu IMC é: {indice:.1f}")

def class_imc(index):
    if index >= 25:
        return print("Acima do peso")
    elif index < 25 and index >= 18.5:
        return print("Peso normal")
    else:
        return print("Abaixo do peso")

classificacao = class_imc(indice)