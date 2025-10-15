def sale(price):
    discount = price * 0.9
    return discount

preco = float(input("Digite o preço do produto: "))
retorno = sale(preco)
print(f"O preço com desconto é: R${retorno:.2f}")