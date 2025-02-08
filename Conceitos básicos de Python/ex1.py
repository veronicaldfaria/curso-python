# 1. Faça um Programa que peça dois números, realize as principais
# operações soma, subtração, multiplicação, divisão

# Solicita dois números ao usuário
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

# Exibe os resultados das operações
print(f'A soma é {num1 + num2}')
print(f'A subtração é {num1 - num2}')
print(f'A multiplicação é {num1 * num2}')

# Verifica se o divisor não é zero antes de dividir
if num2 != 0:
    print(f'A divisão é {num1 / num2}')
else:
    print('Não é possível dividir por zero.')