cardapio = {'Hamburguer': 10, 
            'Hotdog':6.5, 
            'Salada':4,
            'Suco':4, 
            'Refrigerante':4.5, 
            'Água':2}
print(f'Menu FastFood \n {cardapio}')
comida = input('Digite a comida que você deseja: \n')
bebida = input('Digite a bebida que você deseja: \n')
valortotal = cardapio[comida] + cardapio[bebida]
print(f'Seu pedido será: {comida} e {bebida}.\nO valor total será de R${valortotal}')