import time

print('-'*15, '|Contagem Automática|','-'*15)
inicio = int(input('Qual vai ser o início da contagem?\n'))
fim = int(input('A contagem vai até que número?\n'))
passo = int(input('E qual vai ser a soma por intervalo?\n'))
while passo == 0:
        passo = int(input('Digite apenas números maiores que 0 para a soma.\n'))
print('-'*15,'|INTERFACE CONTADOR|','-'*15)
print('-'*54)
def timer():
    time.sleep(0.5)
def contador(num1, num2, num3):
    if inicio < fim:
        for i in range(num1, num2 + 1, num3):
            timer()
            print(i)
    if inicio > fim:
        for i in range(num1, num2 - 1, -num3):
            timer()
            print(i)
contador(inicio, fim, passo)