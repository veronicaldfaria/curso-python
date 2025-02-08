# 8. Solicite ao usuário o número de horas de exercício físico por semana.
# Calcule o total de calorias queimadas em um mês, considerando uma
# média de 5 calorias por minuto de exercício.

# Solicita as horas de exercício por semana
horas_ex_semana = float(input('Digite quantas horas de exercício você faz por semana: '))

# Calcula o número total de minutos de exercício por mês
minutos_semana = horas_ex_semana * 60  # Convertendo horas para minutos
minutos_mes = minutos_semana * 4  # Considerando 4 semanas no mês

# Calorias queimadas por minuto
calorias_por_minuto = 5

# Calcula o total de calorias queimadas no mês
calorias_mes = minutos_mes * calorias_por_minuto

# Exibe o resultado
print(f'Seu consumo mensal de calorias foi de {calorias_mes} calorias.')