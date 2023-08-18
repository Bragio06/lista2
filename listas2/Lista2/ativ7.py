angulo_1 = int(input("Digite o valor do primeiro ângulo: "))
angulo_2 = int(input("Digite o valor do segundo ângulo: "))
angulo_3 = int(input("Digite o valor do terceiro ângulo: "))

soma_dos_angulos = angulo_1 + angulo_2 + angulo_3

if soma_dos_angulos == 180:
    if angulo_1 < 90 and angulo_2 < 90 and angulo_3 < 90:
        resultado = "Acutângulo"
    elif angulo_1 == 90 or angulo_2 == 90 or angulo_3 == 90:
        resultado = "Retângulo"
    elif angulo_1 > 90 or angulo_2 > 90 or angulo_3 > 90:
        resultado = "Obtusângulo"
else:
    resultado = "Os ângulos informados não formam um triângulo"

print(resultado)