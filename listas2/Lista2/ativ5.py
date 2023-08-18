nome_do_aluno= input("Digite o nome do aluno: ")
prava_um = float(input("Digite a nota da primeira prova: "))
prova_dois= float(input("Digite a nota da segunda prova: "))

media_das_provas= (prava_um + prova_dois) / 2

if 0 <= media_das_provas < 5:
    resultado = "Reprovado"

elif 5 <= media_das_provas < 7:
    resultado = "Recuperação"

elif 7 <= media_das_provas <= 10:
    resultado = "Aprovado"

print(f"Nome: {nome_do_aluno}")
print(f"Média: {media_das_provas}")
print(resultado)