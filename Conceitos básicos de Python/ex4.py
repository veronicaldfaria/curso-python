# 4. Receba do usuário a quantidade de litros de combustível consumidos e
# a distância percorrida. Calcule e imprima o consumo médio em km/l.

# Solicita os dados do usuário
litros = float(input('Digite a quantidade de litros de combustível consumidos: '))
distancia = float(input('Digite a distância percorrida em km: '))

# Verifica se os litros consumidos são maiores que zero para evitar erro de divisão por zero
if litros > 0:
    consumo_medio = distancia / litros
    print(f'O consumo médio foi de {consumo_medio:.2f} km/l')
else:
    print('Erro: A quantidade de litros deve ser maior que zero.')