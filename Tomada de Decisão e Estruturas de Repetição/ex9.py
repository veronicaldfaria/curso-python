# 9. O programa deve calcular e apresentar a quantidade de números pares e
# ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
# informar o valor zero. Certifique-se de incluir validações para garantir que
# apenas números positivos sejam considerados na contagem e cálculos.

quant_pares = 0
quant_impares = 0

while True:
    numero = int(input('Digite um número (ou 0 para encerrar): '))
    
    if numero == 0:
        break  # Encerra o loop quando o usuário digitar 0

    if numero > 0:  # Valida se o número é positivo
        if numero % 2 == 0:
            quant_pares += 1  # Incrementa a contagem de números pares
        else:
            quant_impares += 1  # Incrementa a contagem de números ímpares
    else:
        print('Por favor, digite apenas números positivos.')

print(f'Quantidade de números pares: {quant_pares}')
print(f'Quantidade de números ímpares: {quant_impares}')