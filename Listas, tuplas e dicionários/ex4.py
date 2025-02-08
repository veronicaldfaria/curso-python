# 4. Crie um dicionário representando contatos (nome, telefone).
# Permita ao usuário procurar por um contato pelo nome.

# Criando o dicionário para armazenar os contatos
contatos = {
    "Ana": "11987654321",
    "Bruno": "11976543210",
    "Carla": "11965432109",
    "Diego": "11954321098",
    "Eduarda": "11943210987"
}

# Exibindo os contatos disponíveis
print("Lista de contatos disponíveis:")
for nome in contatos:
    print(f"- {nome}")

# Permite ao usuário procurar um contato pelo nome
while True:
    nome = input("\nDigite o nome do contato que deseja procurar (ou 'sair' para finalizar): ").strip().capitalize()
    
    if nome == "Sair":
        break  # Sai do loop se o usuário digitar "sair"
    
    # Verifica se o contato existe
    if nome in contatos:
        print(f"Telefone de {nome}: {contatos[nome]}")
    else:
        print("Contato não encontrado. Tente novamente.")
