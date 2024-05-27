import math
import time
"""
def operacoes(v1):
        return{
        'Fatorial': math.factorial(v1),
        'Inverso': 1/v1,
        'Quadrado': v1**2,
        'RaizQuadrada': math.sqrt(v1)
        }
while True:
    print('-'*15,'|Operações Automáticas|','-'*15)
    num = int(input('Digite um número para fazermos as operações\n'))
    resultado = operacoes(num)
    print(f'Raiz quadrada: {resultado['RaizQuadrada']}\n')
    print(f'Quadrado: {resultado['Quadrado']}\n')
    print(f'Inverso: {resultado['Inverso']}\n')
    print(f'Fatorial: {resultado['Fatorial']}\n')
    sair = input('Digite qualquer coisa para continuar, ou digite 0 para sair\n')
    if sair == '0':
        break
"""
def operacoes(v1):
    if v1 %2 == 0:
        return{
        'Fatorial': math.factorial(v1),
        'Inverso': 1/v1,
        'Quadrado': v1**2,
        'RaizQuadrada': math.sqrt(v1),
        'ParOuImpar': "Par"
        }
    #impar
    elif v1 %2 == 1:
        return{
        'Fatorial': math.factorial(v1),
        'Inverso': 1/v1,
        'Quadrado': v1**2,
        'RaizQuadrada': math.sqrt(v1),
        'ParOuImpar': "Impar"
        } 
while True:
    print('-'*15,'|Operações Automáticas|','-'*15)
    num = (input('Digite um número para fazermos as operações:\n'))
    if num.isdigit():
        num = int(num)
        while num < 1:
          num = int(input('Digite um valor acima de 0:\n'))
        resultado = operacoes(num)
    else:
          continue
    for i in resultado:
            print(f'\n {i} : {resultado[i]} \n')
    sair = input('Digite qualquer coisa para continuar, ou digite 0 para sair\n')
    if sair == '0':
            break
    
        