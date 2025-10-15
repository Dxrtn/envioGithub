def checar(acao):
    try:
            acao = float(acao)
            if acao > 150.99:
                print("Ação está cara! Compre com cuidado.")
            else:
                print("Ação está barata!")
    except ValueError:
            print("Digite um valor válido!")