# import argparse
# parser = argparse.ArgumentParser(description = 'Programa de Soma')
# parser.add_argument('--numeroA', action='store', dest='numA', required=True, help="Primeiro número da soma")

# parser.add_argument('--numeroB', action='store', dest='numB', required=True, help="Segundo número da soma")
# arguments = parser.parse_args()
# a = int(arguments.numA)
# b = int(arguments.numB)

# print(f'{a} + {b} = {a + b}')

listinha = ['a', 'b']
try:
    print(listinha[1])
    algo = int(listinha[1])
except ValueError:
    print('Erro de valor')
except IndexError:
    print('Erro de Index')

while True:
    try:
        x = int(input('Digite um número: \n'))
        break
    except:
        print('Valor inserido é inválido!')

# def exemplo(x):
#     if x < 0:
#         raise StopIteration
#     x = x -1
#     return x

# x = 5

# while True:
#     try:
#         x = exemplo(x)
#         print(x)
#     except:
#         StopIteration
#         break
        

"""
pass -> passa para o próximo
stop iteration -> Mesmo se der erro, "obriga" um erro a aparecer e vai para o fim.
finally -> Vai rodar antes do código fechar

"""

class NovoErro(Exception):
    pass

def exemplo(x):
    if x < 0:
        raise StopIteration
    x = x -1
    return x

x = 5

while True:
    try:
        x = exemplo(x)
        print(x)
    except NovoErro(Exception):
        break



