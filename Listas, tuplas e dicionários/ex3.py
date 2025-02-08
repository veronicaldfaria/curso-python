# 3. Crie um dicionário representando um carrinho de compras.
# Adicione produtos (chaves) e quantidades (valores) ao carrinho.
# Calcule o total do carrinho de compra.

# Criando o dicionário do carrinho de compras
carrinho = {}

# Lista de preços dos produtos disponíveis
precos = {
    "maçã": 2.50,
    "banana": 1.20,
    "leite": 4.50,
    "pão": 3.00,
    "arroz": 10.00
}

# Exibindo os produtos disponíveis
print("Produtos disponíveis e seus preços:")
for produto, preco in precos.items():
    print(f"- {produto.capitalize()}: R$ {preco:.2f}")

# Adicionando produtos ao carrinho
while True:
    produto = input("\nDigite o nome do produto que deseja adicionar (ou 'sair' para finalizar): ").strip().lower()
    
    # Finaliza o processo de adicionar itens
    if produto == "sair":
        break
    
    # Verifica se o produto está disponível
    if produto in precos:
        quantidade = int(input(f"Digite a quantidade de {produto}: "))
        
        # Se o produto já está no carrinho, soma a quantidade
        if produto in carrinho:
            carrinho[produto] += quantidade
        else:
            carrinho[produto] = quantidade
    else:
        print("Produto não encontrado. Tente novamente.")

# Calculando o total da compra
total = sum(precos[produto] * quantidade for produto, quantidade in carrinho.items())

# Exibindo os itens comprados e o total da compra
print("\nResumo da compra:")
for produto, quantidade in carrinho.items():
    print(f"- {produto.capitalize()}: {quantidade} unidade(s) - Total: R$ {precos[produto] * quantidade:.2f}")

print(f"\nValor total da compra: R$ {total:.2f}")
