import argparse
import re

# Escolha de variável/argumento
parser = argparse.ArgumentParser(description = 'Manipulação de Textos 2.0')
parser.add_argument('--file', action='store', dest='file_path', required=False, help='Arquivo para ser aberto e analisado.')
parser.add_argument('--file2', action='store', dest='file_path2', required=False, help='Arquivo para mandar as palavras divididas e mostrar quantas vezes apareceu a palavra escolhida.')
parser.add_argument('--string', action='store', dest='palavra', required=True, help='Palavra para ser encontrada e somar as repetições.')

arguments = parser.parse_args()
arquivoLeitura = arguments.file_path
arquivoWrite = arguments.file_path2
palavraBusca = arguments.palavra

# Se não for especificado o arquivo
if arquivoLeitura == None:
    arquivoLeitura = 'Ex21.txt'
if arquivoWrite == None:
    arquivoWrite = 'manipulArquivo.txt'

# Leitura do arquivo e divisão por palavras.
arquivo = open(arquivoLeitura, encoding='utf8', mode='r')
lista = []
p = arquivo.read().strip()
palavras = re.split(r'[\s\n,.]+',p.lower())

# Adição das palavras na lista e organização por ordem alfabética
for i in palavras:
    lista.append(palavras)
palavrasDistintas = list(set(palavras))
palavrasDistintas.sort()
arquivo.close()

# Contagem da Palavra escolhida
contagem = 0
for palavra in palavras:
    if palavra == palavraBusca:
        contagem += 1

# Write no segundo arquivo
arquivo2 = open(arquivoWrite, encoding='utf8', mode='w+')
arquivo2.write(f'No primeiro arquivo há {len(palavrasDistintas)} palavras diferentes.\n')
arquivo2.write('Sendo elas:\n')

# Divisão por linha 
for i in range(0, len(palavrasDistintas), +1):
    arquivo2.write(f'{palavrasDistintas[i]}\n')

# Write da palavra escolhida e quantas vezes apareceu
arquivo2.write(f'A palavra escolhida foi \'{palavraBusca}\'. Ela apareceu {contagem} vezes no primeiro arquivo.')
print(contagem)