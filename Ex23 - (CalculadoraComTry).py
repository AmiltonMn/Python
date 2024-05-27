print('-'*15,'|CALCULADORA|', '-'*15)
while True:
        while 1:
            # Try para resolver divisão por zero e erros com strings em variáveis
            try:
                n1 = int(input('Digite o primeiro número: '))
                n2 = int(input('Digite o segundo número: '))
                escolha = int(input('Digite qual operação você quer realizar\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n0 - Sair\n'))
                # If's para operações
                if escolha == 1:
                    soma = n1 + n2
                    print(f'O resultado é de: {soma}')
                elif escolha == 2:
                    sub = n1 - n2
                    print(f'O resultado é: {sub}')
                elif escolha == 3:
                    mult = n1 * n2
                    print(f'O resultado é: {mult}')
                try:
                    if escolha == 4:
                        div = n1 / n2
                        print(f'O resultado é: {div}')
                except ZeroDivisionError:
                    print('O número não pode ser dividido por zero!')
                if escolha == 0:
                    break
                sair = int(input('Digite 0 se quiser sair, para continuar digite qualquer número: '))
                if sair == 0:
                    break
            # Except para valores inseridos que não são int
            except ValueError:
                print('O valor inserido não é um número!')
        break