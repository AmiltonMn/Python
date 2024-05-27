nome = str(input('Digite seu nome completo? (Digite com letras minusculas) '))

print(f'Olá, {nome.title()}\nSeu nome tem {len(nome.replace(' ', ''))} caracteres')