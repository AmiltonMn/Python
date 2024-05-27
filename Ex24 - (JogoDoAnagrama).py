import random
import time
import re
pontos = 100
sair = 0
nivel = 1
def tempo():
    time.sleep(0.5)

     
# Escolha do nivel
while True:
    try:
        nivel = int(input('Qual nível você gostaria de jogar?\n---------------\nNível 1 - Fácil: as palavras possuem no máximo 6 letras\n---------------\nNível 2 - Médio: são palavras normais com +6 letras\n---------------\nNível 3 - Difícil: Palavras difíceis e as vezes extensas\n---------------\nNível 4 - Aleatório: Iremos te dar uma dificuldade aleatória para jogar\n---------------\n(Para selecionar o nível, digite o número dele. Ex: se for jogar o nível 1, digite \'1\')\n'))
        if nivel <1 or nivel >4:
            print('Digite apenas números entre 1 e 4!')
            raise ValueError
        else:
            break
    except ValueError:
        print('Digite apenas números válidos para selecionar o nível!!! (Números entre 1 e 4)\n\n')
        tempo()     

    
while True:
    # Escolha dos níveis
    if nivel == 1:
        abrir = 'nivel1.txt'
    if nivel == 2:
        abrir = 'nivel2.txt'
    if nivel == 3:
        abrir = 'nivel3.txt'
    if nivel == 4:
        nivel = random.randint(1,3)
        print(f'O nível escolhido foi o nivel {nivel}')
        if nivel == 1:
            abrir = 'nivel1.txt'
        elif nivel ==2:
            abrir = 'nivel2.txt'
        elif nivel ==3:
            abrir = 'nivel3.txt'

    arquivo = open(abrir, encoding='utf8', mode='r') # Abertura do arquivo

    palavrasArquivo1 = arquivo.read().strip() # Divide as palavras do arquivo

    facil = re.split(r'[\n\s.]+',palavrasArquivo1.lower()) # Adiciona as palavras em uma lista e deixa em lower

    palavra = random.choice(facil) # Escolhe uma palavra aleatória da lista

    palavraDividida = (','.join(palavra)) # Divide as letras colocando virgulas

    palavraDividida = palavraDividida.split(',') # Tira as vírgulas e deixa apenas as letras na lista

    random.shuffle(palavraDividida) # "Bagunça" a palavra

    anagrama = ' '.join(palavraDividida) # Separa as letras por um espaço

    # Parte do jogo
    while True:
        print(anagrama.upper())
        try:
            print(f'PONTUAÇÃO: {pontos}')
            palpite = str(input('Digite seu palpite: '))
        except TypeError:
            print('Digite apenas palavras!')
        if palpite == palavra:
                pontos += 10
                print('Parabéns você acertou a palavra!!\n','-'*30)
                sair = str(input('Quer continuar jogando?\nSe sim, digite qualquer coisa:\nSe não, digite 0:\n'))
                break
        if palpite != anagrama:
                pontos -=10
        if pontos == 0:
                print('Você perdeu :(')
                break
    if sair == '0':
        break