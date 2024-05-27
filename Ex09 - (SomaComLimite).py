limite = int(input('Digite até qual número você quer fazer a soma: '))
soma = 0
cont = 1
while cont <= limite:
    print(soma)
    soma = soma + cont
    cont = cont + 1
print(f'A soma dos números é de {soma}')
