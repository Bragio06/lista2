mes_no_ano = int(input("Informe o número do mês: "))
ano = int(input("Informe o ano: "))

dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    dias_por_mes[2] = 29

if 1 <= mes_no_ano <= 12:
    print(f"O mês {mes_no_ano}/{ano} possui {dias_por_mes[mes_no_ano]} dias.")
else:
    print("Mês inválido. Por favor, informe um número de mês válido (1-12).")
    