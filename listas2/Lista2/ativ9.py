sexo_da_pessoa= input("Informese você é homen ou mulher: ")
peso_da_pessoa= float(input("Informe o peso (kg): "))
altura_da_pessoa_em_cm = int(input("Informe a altura (cm): "))
idade_da_pessoa= int(input("Informe a idade: "))

if sexo_da_pessoa == "homen":
    calorias_ideais = 66 + (13.7 * peso_da_pessoa) + (5.0 * altura_da_pessoa_em_cm) - (6.8 * idade_da_pessoa)
    print(f"O valor ideal de calorias diárias para os homens é: {calorias_ideais} calorias")

else:
    calorias_ideais = 665 + (9.6 * peso_da_pessoa) + (1.8 * altura_da_pessoa_em_cm) - (1.7 * idade_da_pessoa)
    print(f"O valor ideal de calorias diárias para as mulheres é: {calorias_ideais} calorias")