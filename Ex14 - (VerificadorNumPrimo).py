print('-'*30)
print('Verificador de Números Primos')
print('-'*30)
n = int(input('Digite um número: \n'))
lista = []
for i in range(1, n+1):
    if n %i == 0:
        lista.append(i)
print(lista)
if len(lista) == 2:
    print(f'O número {n} é um número primo')
else:
    print(f'O número {n} não é um número primo')
