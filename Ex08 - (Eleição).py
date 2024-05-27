nome = str(input('Qual o seu nome? \n'))
nasc = input('Qual seu ano de nascimento? ')
nasc = int(nasc)
idade = 2024 - nasc
if idade <16:
    print(f'{nome} você não pode votar!')
if idade >=16 and idade <18 or idade >70:
    print(f'{nome} seu voto é facultativo!')
if idade >= 18 and idade <=70:
    print(f'{nome} seu voto é obrigatório!')