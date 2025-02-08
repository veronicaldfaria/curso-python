# 3. Escreva um script que pergunta ao usuário se ele deseja converter
# uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
# cada opção, crie uma função.
# Plus: Crie uma terceira, que é um menu para o usuário escolher a opção
# desejada, onde esse menu chama a função de conversão correta.

# Função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Função para converter Fahrenheit para Celsius
def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Função que exibe o menu e chama a conversão correta
def menu():
    while True:
        print("\nConversor de Temperatura")
        print("1 - Converter Celsius para Fahrenheit")
        print("2 - Converter Fahrenheit para Celsius")
        print("3 - Sair")
        
        opcao = input("Escolha uma opção (1, 2 ou 3): ")

        if opcao == "1":
            celsius = float(input("Digite a temperatura em Celsius: "))
            resultado = celsius_para_fahrenheit(celsius)
            print(f"{celsius}°C equivalem a {resultado:.2f}°F")
        elif opcao == "2":
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            resultado = fahrenheit_para_celsius(fahrenheit)
            print(f"{fahrenheit}°F equivalem a {resultado:.2f}°C")
        elif opcao == "3":
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

# Chamada do menu para iniciar o programa
menu()