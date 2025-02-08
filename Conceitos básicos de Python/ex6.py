# 6. Solicite ao usuário o peso em kg e a altura em metros. Calcule e
# imprima o Índice de Massa Corporal (IMC) usando a fórmula:
# IMC = peso / (altura x altura).

# Solicita os dados do usuário
peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))

# Verifica se os valores são válidos
if peso <= 0 or altura <= 0:
    print('Erro: O peso e a altura devem ser maiores que zero.')
else:
    # Calcula o IMC
    imc = peso / (altura ** 2)

    # Determina a classificação do IMC
    if imc < 18.5:
        classificacao = 'Abaixo do peso'
    elif 18.5 <= imc < 24.9:
        classificacao = 'Peso normal'
    elif 25 <= imc < 29.9:
        classificacao = 'Sobrepeso'
    elif 30 <= imc < 34.9:
        classificacao = 'Obesidade grau I'
    elif 35 <= imc < 39.9:
        classificacao = 'Obesidade grau II'
    else:
        classificacao = 'Obesidade grau III (mórbida)'

    # Exibe o resultado
    print(f'Seu IMC é {imc:.2f}. Classificação: {classificacao}')