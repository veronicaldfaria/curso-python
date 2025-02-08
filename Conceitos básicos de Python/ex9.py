# 9. Faça um Programa que utilize 4 variáveis como preferir e no final print
# uma mensagem amigável utilizando as variáveis criadas.
# Exemplos de variáveis: nome, idade, lugar, profissão ....
# Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo
# também e estou migrando de área.
# Lembrando que para o retorno vamos usar print com as variáveis
# criadas e este texto é somente um exemplo, utilizem a criatividade.

# Solicita as informações ao usuário
nome = input('Qual é o seu nome? ')
idade = int(input('Quantos anos você tem? '))
cidade = input('De onde você é? ')
profissao = input('Qual é a sua profissão? ')

# Exibe a mensagem amigável com as informações fornecidas
print(f'Olá! Meu nome é {nome}, eu tenho {idade} anos, sou de {cidade} e trabalho como {profissao}. Até logo!')