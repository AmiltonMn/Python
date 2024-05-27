import re

# Leitura do arquivo e divisão por palavras.
arquivo = open('Ex21.txt', encoding='utf8', mode='r')
lista = []
p = arquivo.read().strip()
palavra = re.split(r'[\s\n,.'']+',p.lower())
print(palavra)

# Adição das palavras na lista e organização por ordem alfabética
for i in palavra:
    lista.append(palavra)
palavrasDistintas = list(set(palavra))
palavrasDistintas.sort()
print(palavrasDistintas[0])
print(palavrasDistintas)
print(len(palavrasDistintas))
arquivo.close()

arquivo2 = open('Ex21(2).txt', encoding='utf8', mode='w+')
arquivo2.write(f'No primeiro arquivo há {len(palavrasDistintas)} palavras diferentes.\n')
arquivo2.write('Sendo elas:\n')
for i in range(1, len(palavrasDistintas), +1):
    arquivo2.write(f'{palavrasDistintas[i]}\n')
arquivo2.read()