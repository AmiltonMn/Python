import random
frases_tristes = ['Que pena que você me odeia!\nAté nunca mais.', 'Que triste que você está indo embora :(\nAté mais! :/', 'Eu vou te esperaaar, aonde quer que eu vá!', 'A casa é grande demais, vazia demais comigo...\nSentirei sua falta!', 'Então eu ficarei aqui novamente... Sozinho.', 'E no final, eu dou tudo a eles, e o que me sobra, é solidão...']
while True:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    escolha = int(input('Digite qual operação você quer realizar\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n0 - Sair\n'))
    if escolha == 1:
        soma = n1 + n2
        print(f'O resultado é de: {soma}')
    elif escolha == 2:
        sub = n1 - n2
        print(f'O resultado é: {sub}')
    elif escolha == 3:
        mult = n1 * n2
        print(f'O resultado é: {mult}')
    elif escolha == 4:
        div = n1 / n2
        print(f'O resultado é: {div}')
    elif escolha == 0:
        print(random.choice(frases_tristes))
        break
    sair = int(input('Digite 0 se quiser sair, para continuar digite qualquer número: '))
    if sair == 0:
        print(random.choice(frases_tristes))
        break