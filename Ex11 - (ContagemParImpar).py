print('---------------------\nContagem de Números Pares\n---------------------')
i = int(input('Digite um número para começar a contagem:\n'))
limite = int(input('E qual será o final da contagem?\n'))
for i in range(i, limite):
    if i %2 == 0:
        print(i)
print('Agora vamos fazer a contagem dos Ímpares:\n')
print('---------------------\nContagem de Números Ímpares\n---------------------')
i = int(input('Qual vai ser o novo número de início?\n'))
limite = int(input('E qual será o novo limite?\n'))
for i in range (i, limite):
    if i %2 == 1:
        print(i)
print('Muito obrigado! :)')


