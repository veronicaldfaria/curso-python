# 5. Escreva um programa que calcule o tempo de uma viagem. Faça um
# comparativo do mesmo percurso de avião, carro e ônibus.
# Levando em consideração:
# ● avião = 600 km/h
# ● carro = 100 km/h
# ● ônibus = 80 km/h

# Solicita a distância do percurso ao usuário
percurso = float(input('Digite o percurso a ser percorrido em km: '))

# Velocidades em km/h
velocidade_aviao = 600
velocidade_carro = 100
velocidade_onibus = 80

# Cálculo do tempo de viagem
tempo_aviao = percurso / velocidade_aviao
tempo_carro = percurso / velocidade_carro
tempo_onibus = percurso / velocidade_onibus

# Exibe os tempos formatados
print(f'De avião irá demorar aproximadamente {tempo_aviao:.2f} horas.')
print(f'De carro irá demorar aproximadamente {tempo_carro:.2f} horas.')
print(f'De ônibus irá demorar aproximadamente {tempo_onibus:.2f} horas.')