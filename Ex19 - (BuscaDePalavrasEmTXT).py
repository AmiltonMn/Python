
arquivo = open('arquivo.txt', 'w')
arquivo.write('Esse e o tal jogo que e melhor que o god of war 4 de usuario para ter uma ideia de como fazer um orcamento para limpar o nome da empresa para que eu possa fazer um novo anuncio')
arquivo.write('\nJogo Jogo Jogo Jogo Jogo')
arquivo.write('\nEsse Esse Esse Esse Esse')
arquivo.write('\nBom dia Bom dia Bom dia Bom dia')
palavra_usuario = input('Digite qual palavra você quer pesquisar no arquivo:\n')
print('-'*50)
arquivo.close()

arquivo = open('arquivo.txt', 'r')

contagem = 0
for palavra in arquivo:
    print(palavra)
    palavra = palavra.strip()
    palavra = palavra.split(' ')
    for i in palavra:
        if i == palavra_usuario:
            contagem += 1
print(f'A palavra {palavra_usuario} aparece {contagem} vezes.')




