nome_1  = input("Digite o nome da primeira pessoa: ")
data_1 = input("Digite a data de nascimento da primeira pessoa: ")

nome_2  = input("Digite o nome da segunda pessoa: ")
data_2 = input("Digite a data nascimento da segunda pessoa: ")

ano_data_um = data_1[6:10]
ano_data_dois = data_2[6:10]

ano_atual = int(input("Digite o ano atual: "))

ano_data_um = int(ano_data_um)
ano_data_dois = int(ano_data_dois)

ano_nascimento_um = ano_atual - ano_data_um
ano_nascimento_dois = ano_atual - ano_data_dois

if data_1 < data_2:
    print(f"A pessoa mais nova é {nome_1} é tem {ano_nascimento_um}.")
elif data_2 < data_1:
    print(f"A pessoa mais nova é {nome_2} é tem {ano_nascimento_dois}.")
else:
    print("As duas pessoas têm a mesma idade.")
