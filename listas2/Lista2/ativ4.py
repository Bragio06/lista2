numero_um = int(input("Digite o primeiro número: "))
numero_dois = int(input("Digite o segundo número: "))
numero_três = int(input("Digite o terceiro número: "))

if numero_um > numero_dois and numero_um > numero_três:
    print(f"O maior número é: {numero_um}")
elif numero_dois > numero_três:
    print(f"O maior número é: {numero_dois}")
else:
    print(f"O maior número é: {numero_três}")
 