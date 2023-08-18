sexo_da_pessoa = input("Informe o sexo se é masculino ou feminino : ")
idade_da_pessoa= int(input("Informe a idade: "))

if sexo_da_pessoa == "masculino":
    if idade_da_pessoa >= 21:
        print("Maior idade")
    else:
        print("Menor idade")
elif sexo_da_pessoa == "feminino":
    if idade_da_pessoa >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")