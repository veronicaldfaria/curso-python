# 7. Faça um Programa que pergunte quanto você ganha por hora e o
# número de horas trabalhadas no mês. Calcule e mostre o total do seu
# salário no referido mês.

# Solicita os dados do usuário
salario_hora = float(input('Digite quanto você ganha por hora: '))
horas_mes = float(input('Digite quantas horas você trabalhou no mês: '))

# Verifica se os valores são válidos
if salario_hora <= 0 or horas_mes <= 0:
    print('Erro: O valor do salário por hora e as horas trabalhadas devem ser maiores que zero.')
else:
    # Calcula o salário mensal
    salario_mensal = salario_hora * horas_mes

    # Exibe o resultado formatado
    print(f'O salário do mês foi de R$ {salario_mensal:.2f}')