# 7. Desenvolver um programa que solicite a idade do usuário e identifique se
# ele é uma criança, um adolescente, adulto ou idoso.

idade = int(input('Digite sua idade:'))

if idade >= 1 and idade <= 10:
    print('Você é criança')
elif idade >= 11 and idade <= 19:
    print('Você é adolescente')
elif idade >= 20 and idade <= 59:
    print('Você é adulto')
elif idade >= 60:
    print('Você é idoso')