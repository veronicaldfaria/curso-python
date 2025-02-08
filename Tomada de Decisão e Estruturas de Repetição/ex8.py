# 8. Criar um programa em Python que solicite três números ao usuário, utilize
# estruturas condicionais para determinar o maior entre eles e apresente o
# resultado.

num1 = int(input('Digite um número:'))
num2 = int(input('Digite outro número:'))
num3 = int(input('Digite mais um número:'))

# Verifica o maior número, incluindo a possibilidade de empates
if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2)
else:
    print(num3)