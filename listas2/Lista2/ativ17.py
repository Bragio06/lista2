valor_de_z = float(input("qual o valor de z: "))
valor_de_w = float(input("qual o valor de w: "))



if valor_de_w < 0 and valor_de_z <  7:
    x = (5*valor_de_w + 1)/3
    t = 5 * valor_de_z + 2
    y = 7 * x **3 - 3 * x **0.5 - 8 * t / 5 * (x + 1)
    print(f"O valor de X é {x},o do T é {t} e o de Y é {y}")
else:
    x = 5 *  valor_de_z + 2
    t =  (5*valor_de_w + 1)/3
    y = 7 * x **3 - 3 * x **0.5 - 8 * t / 5 * (x + 1)
    print(f"O valor de X é {x},o do T é {t} e o de Y é {y}")
