print('-'*15,'|CADASTRO DE CASA|','-'*15)
class casa():
    def __init__(self, area, rua, cor, nome):
        self.area = area
        self.rua = rua
        self.cor = cor
        self.nome = nome
    def cadastro_atributos():
        while True:
            try:
                cadastro_nome = int(input('Gostaria de cadastrar seu nome? Se sim, digite 1. Se não, digite 0\n'))
                if cadastro_nome == 1:
                    casa.nome = str(input('Digite seu nome: \n'))
                    break
                if cadastro_nome == 0:
                    casa.nome = 'Não Informado'
                    break
            except ValueError:
                print('Digite um número válido')
        casa.area = int(input('Qual a área da sua casa?\n'))
        casa.rua = str(input('Qual a rua da sua casa?\n'))
        casa.cor = str(input('Qual a cor da sua casa?\n'))
    def mostrar_atributos():
        print(f'Sua casa tem {casa.area}M² e é localizada na rua {casa.rua}. A cor da sua casa é {casa.cor} e seu nome é {casa.nome}.')
casa.cadastro_atributos()
casa.mostrar_atributos()