import random
v = 0
d = 0
r = 0
vs = 0
while True:
    print('-'*15, 'IMPAR OU PAR', '-'*15)
    J = str(input('Você escolhe Ímpar ou Par?\n')).lower()
    C = random.randint(1, 100)
    Jn = int(input('Qual número você escolhe? (De 1 a 100)\n'))
    while not Jn > 0 or Jn > 100:
            Jn = int(input('Digite apenas números que estão entre 0 e 100\n'))
    res = Jn + C
    print('\n')
    if res %2 == 0:
        if J == 'par' or J == 'par':
            print(f'Você escolheu {J} e escolheu o número {Jn}. O computador escolheu {C}. O resultado foi de: {res}')
            print('Você venceu! :D\n')
            v = v + 1
            vs = vs + 1
        else:
            print(f'Você escolheu {J} e escolheu o número {Jn}. O computador escolheu {C}. O resultado foi de: {res}')
            print('Você perdeu! :(\n')
            d = d + 1
            vs = 0
    elif res %2 == 1:
        if J == 'impar' or J == "ímpar":
            print(f'Você escolheu {J} e escolheu o número {Jn}. O computador escolheu {C}. O resultado foi de: {res}')
            print('Você venceu! :D\n')
            v = v + 1
            vs = vs + 1
        else:
            print(f'Você escolheu {J} e escolheu o número {Jn}. O computador escolheu {C}. O resultado foi de: {res}')
            print('Você perdeu! :(\n')
            d = d + 1
            vs = 0
    if vs >= r:
        r = vs
    print(f'VITORIAS: {v}\n')
    print(f'DERROTAS: {d}\n')
    print(f'VITORIAS SEGUIDAS: {vs}\n')

    print(f'RECORD VITORIAS SEGUIDAS: {r}\n')
    jogo = (input('Jogar Novamente? Se sim digite qualquer coisa, se não, digite 0\n'))
    if jogo == '0':
        break
    