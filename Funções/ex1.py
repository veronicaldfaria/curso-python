# 1. Faça um programa, com uma função que necessite de três
# argumentos, e que forneça a soma desses três argumentos.

# Função que recebe três números como argumentos e retorna a soma deles
def somar(a, b, c):
    return a + b + c

# Solicita os três números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Chama a função e exibe o resultado
resultado = somar(num1, num2, num3)
print(f"A soma dos três números é: {resultado}")