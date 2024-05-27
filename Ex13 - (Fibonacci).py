print('-'*25)
print('Série de Fibonacci')
print('-'*25)
limite = int(input('Escolha qual será o limite para a sequência de Fibonnaci\n'))
fibo = 0
nacci = 1
esp = 1

print('\n')
for i in range (limite):
   if i == 0:
      print(' ',fibo)
   if i == 1:
      print('  ', nacci)
   if i >= 2:
      esp = esp + 1
      seq = fibo + nacci
      fibo = nacci
      nacci = seq
      print(' '*esp, nacci)


