# 3. Faça um programa que peça uma nota, entre zero e dez. Mostre uma
# mensagem caso o valor seja inválido e continue pedindo até que o usuário
# informe um valor válido.

# Solicita a nota ao usuário
nota = int(input('Digite uma nota de 0 a 10:'))

# Continua pedindo até que a nota seja válida
while nota < 0 or nota > 10:
    print('Nota inválida. Tente novamente.')
    nota = int(input('Digite uma nota de 0 a 10:'))

# Quando a nota for válida, exibe a mensagem
print('Nota válida.')