# 1. Faça um Programa que peça dois números e imprima o maior deles.

# Solicita os números ao usuário
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

# Verifica qual número é maior
if num1 > num2:
    print(f'O maior número é {num1}.')
elif num1 < num2:
    print(f'O maior número é {num2}.')
else:
    print('Os dois números são iguais.')