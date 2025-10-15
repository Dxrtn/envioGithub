def menor_maior_idade(age):
    if age >= 18:
        return print("Maior de idade")
    elif age == 0:
        return print("idade não pode ser 0")
    else:
        return print("Menor de idade")
    
idade = int(input("Digite sua idade: "))
menor_maior_idade(idade)