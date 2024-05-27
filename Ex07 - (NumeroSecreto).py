numerosecreto = 42
chance = 0
palpite = input('Tente adivinhar o número: ')


if palpite.isdigit():
        palpite=int(palpite)
        if palpite == numerosecreto:
                print('Parabéns! Você acertou o número!')
        else:
                print('Você errou o número!')
else:
    print('Digite apenas números!')

