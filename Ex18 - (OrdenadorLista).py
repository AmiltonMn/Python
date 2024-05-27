from random import randint
limiteInferior = int(input('Digite o limite inferior (Digite apenas números!): \n'))
limiteSuperior = int(input('Digite o limite superior (Digite apenas números!): \n'))
tamanhoLista = int(input('Digite o tamanho da lista (Digite apenas números!): \n'))
def ordem(v1,v2,v3):
    list = [randint(v1,v2) for i in range(v3)]
    print('Lista Original:')
    print(list)
    print('-'*50)
    for i in range(v3):
        for j in range(v3-1):
            if list[j] > list[j+1]:
                troca = list[j]
                list[j] = list[j+1]
                list[j+1] = troca
print('Lista Crescente')
print('-'*50)
print(list)
list.reverse()
print('Lista Decrescente')
print('-'*50)
print(list)
ordem(limiteInferior,limiteSuperior,tamanhoLista)