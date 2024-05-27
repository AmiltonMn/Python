import time
"""
for i in range (10):
    print(i)

    r:
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9

lista = ['item_a', 'item_b','item_c', 'item_d']
for i in lista:
    print(i)

    r:
    item_a
    item_b
    item_c
    item_d

for i in range (2,10,2):
    print(i)

    r:
    2
    4
    6
    8



for i in range(5):
    for j in range(5):
        print('#', end = '')
    print('@', end = '')

    r:
    #####@#####@#####@#####@#####@

def saudações():
    print('Bom dia!')
"""

"""Caso você queira fazer uma função que altera uma variável de forma global, utilize o comando \global/
X = 5
def funcao():
    X = 2
    print(X)
funcao()
print(X)

x = 5
def funcao():
    global X
    x = 2
    print(x)
funcao()
print(x)
"""
"""Na segunda forma, a função vai retornar o valor V. Na primeira ele apenas printa, dentro da função, o valor de V.
    v = distancia/tempo
    print(v)

def velocidade(distancia,tempo):
    v =distancia/tempo
    return v
resultado = velocidade(100,2)
print(resultado)
"""
"""Caso na função o parâmetro não tenha um parâmetro com variável definido, ele irá retornar o que está dentro do parâmetro, caso seja especificado.
def ola(nome='estranho'):
    print(f'Olá, {nome}')
ola()
"""
x = 0
y = 1
def calculadora(x=1,y=2):
    return x+y, x-y
calculadora()