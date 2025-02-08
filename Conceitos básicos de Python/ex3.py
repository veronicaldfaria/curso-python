# 3. Faça um Programa que peça a quantidade de quilômetros, transforme
# em metros, centímetros e milímetros.

# Solicita a quantidade de quilômetros
km = float(input('Digite uma quantidade de km: '))

# Converte e exibe os resultados
print(f'Em metros: {km * 1000} m')
print(f'Em centímetros: {km * 100000} cm')
print(f'Em milímetros: {km * 1000000} mm')