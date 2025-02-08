# 5. Desenvolva um programa que solicite ao usuário os comprimentos dos três
# lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
# equilátero: todos os lados com o mesmo valor
# isósceles: dois lados com o mesmo valor
# escaleno: todos os lados com medidas distintas.

# Solicita os lados ao usuário
lado1 = int(input('Digite o valor do lado 1 do triângulo:'))
lado2 = int(input('Digite o valor do lado 2 do triângulo:'))
lado3 = int(input('Digite o valor do lado 3 do triângulo:'))

# Verifica se os lados formam um triângulo válido
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    # Classifica o triângulo
    if lado1 == lado2 and lado2 == lado3:
        print('O triângulo é equilátero.')
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print('O triângulo é isósceles.')
    else:
        print('O triângulo é escaleno.')
else:
    print('Os lados informados não formam um triângulo válido.')