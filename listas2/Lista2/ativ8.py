distancia_em_km    = float(input("Digite a distância percorrida em Km: "))
litros_de_gasolina = float(input("Digite a quantidade de litros de gasolina consumidos: "))

consumo_km_por_litro = distancia_em_km / litros_de_gasolina


if consumo_km_por_litro < 8:
    print(f"O consumo do carro é de {consumo_km_por_litro:.2f} Km/l.Venda o carro!")

elif consumo_km_por_litro >= 8 and consumo_km_por_litro <= 14:
    print(f"O consumo do carro é de {consumo_km_por_litro:.2f} Km/l.Econômico!")
    
else:
    print(f"O consumo do carro é de {consumo_km_por_litro:.2f} Km/l.Super econômico!")