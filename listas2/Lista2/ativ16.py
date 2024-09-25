numero = int(input("Informe um número de 3 dígitos: "))

if 100 <= numero <= 999:
    digito_1 = numero // 100
    digito_2 = (numero // 10) % 10
    digito_3 = numero % 10

    soma_dos_digitos = digito_1 + digito_2 + digito_3

    print(f"Soma dos dígitos do número {numero} é igual a {soma_dos_digitos}")

    numero_novo= digito_1 * 100 + digito_2 * 10 + digito_3

    if numero_novo % 16 == 0 and numero_novo % 4 == 0:
        print("O número informado é divisor de 16 e múltiplo de 4 ao mesmo tempo.")
    else:
        print("O número informado não satisfaz as condições.")
else:
    print("Número fora do intervalo de três dígitos.")
    