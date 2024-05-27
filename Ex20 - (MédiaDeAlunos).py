import math
arquivo = open('dados.txt', encoding='utf8', mode='w+')
nomes = []
notas = []
alunosNotas = {}
maioresMedias = []
quantidadeNotas = 0
quantidadeAlunos = int(input('De quantos alunos você quer fazer a média?\n'))

# Quantidade de alunos
for i in range(quantidadeAlunos):
     alunos = str(input(f'Qual o nome do(a) {i+1}° aluno(a)?\n'))
     nomes.append(alunos)

# Input Notas
quantidadeNotas=int(input('Quantas notas serão utilizadas, por aluno, para fazer a média?\n'))
for i in range(quantidadeAlunos):
    for j in range(0,quantidadeNotas, +1):
        notasLista = float(input(f'Qual a {j+1}° nota do(a) aluno(a) {nomes[i]}?\n'))
        notas.append(notasLista)
maiorMedia = 0
float(maiorMedia)
finalNotas = 0
j = 0

# Write no arquivo, media e maior media
for i in range(0, quantidadeAlunos, +1):
    finalNotas += quantidadeNotas
    soma = float(sum(notas[j:finalNotas]))
    media = soma/quantidadeNotas
    arquivo.write(f'As notas do(a) aluno (a) {nomes[i]} são: {notas[j:finalNotas]}. E a média dele(a) foi de {media}\n')
    if media >= 7:
        print(f'O aluno {nomes[i]} foi APROVADO\n')
        print(media)
        arquivo.write(f'O(a) aluno(a) {nomes[i]} foi APROVADO\n')
        maiorMedia = media
        maioresMedias.append(nomes[i])
        if media > maiorMedia:
            maiorMedia = media
            maioresMedias.remove(nomes[0])
            maioresMedias.append(nomes[i])
    else:
        print(f'O aluno {nomes[i]} foi REPROVADO')
        print(media)
        arquivo.write(f'O(a) aluno(a) {nomes[i]} foi REPROVADO\n')
    j += quantidadeNotas
print(maioresMedias)
arquivo.write(f'A maior média foi do aluno: {maioresMedias[0]}. Sua média foi de {maiorMedia}.')