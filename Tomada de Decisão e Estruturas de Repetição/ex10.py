# 10. Faça um programa que lê três números inteiros e os mostra em ordem
# crescente.

num1 = int(input('Digite um número:'))
num2 = int(input('Digite outro número:'))
num3 = int(input('Digite mais um número:'))

# Compara os números manualmente para colocá-los em ordem crescente
if num1 <= num2 and num1 <= num3:
    if num2 <= num3:
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)
elif num2 <= num1 and num2 <= num3:
    if num1 <= num3:
        print(num2, num1, num3)
    else:
        print(num2, num3, num1)
else:
    if num1 <= num2:
        print(num3, num1, num2)
    else:
        print(num3, num2, num1)