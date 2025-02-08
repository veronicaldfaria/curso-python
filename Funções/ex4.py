# 4. Crie um programa que leia quanto dinheiro uma pessoa tem na
# carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
# Considere a tabela de conversão abaixo:
# Dólar Americano: R$ 4,91
# Peso Argentino: R$ 0,02
# Dólar Australiano: R$ 3,18
# Dólar Canadense: R$ 3,64
# Franco Suiço: R$ 0,42
# Euro: R$ 5,36
# Libra esterlina: R$ 6,21

# Dicionário com as taxas de câmbio
taxas_cambio = {
    "Dólar Americano": 4.91,
    "Peso Argentino": 0.02,
    "Dólar Australiano": 3.18,
    "Dólar Canadense": 3.64,
    "Franco Suíço": 0.42,
    "Euro": 5.36,
    "Libra Esterlina": 6.21
}

# Solicita ao usuário o valor em reais
dinheiro_reais = float(input("Quanto dinheiro você tem na carteira (em R$)? "))

# Calcula e exibe o valor convertido para cada moeda
print("\nCom R$ {:.2f}, você pode comprar:".format(dinheiro_reais))
for moeda, taxa in taxas_cambio.items():
    valor_convertido = dinheiro_reais / taxa
    print(f"- {valor_convertido:.2f} {moeda}")