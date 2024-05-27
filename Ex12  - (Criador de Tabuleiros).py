print('---------------------------\nCriador de Tabuleiros\n---------------------------')
y = int(input('Qual a quantidade de colunas que o tabuleiro terá?\n'))
x = int(input('E qual a quantidade de linhas?\n'))
if x < 1 or y < 1:
   print('Favor inserir números maiores que 0')
   y = int(input('Qual a quantidade de colunas que o tabuleiro terá?\n'))
   x = int(input('E qual a quantidade de linhas?\n\n'))
for i in range (x):
    for j in range (y):
        print('X ', end = '')
    print(' ')
