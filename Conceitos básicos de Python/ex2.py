# 2. Peça ao usuário para informar o ano de nascimento. Em seguida,
# calcule e imprima a idade atual.

from datetime import datetime

# Obtém o ano atual dinamicamente
ano_atual = datetime.now().year

# Solicita o ano de nascimento
ano_nasc = int(input('Digite seu ano de nascimento: '))

# Valida o ano informado
if ano_nasc > ano_atual:
    print('Erro: O ano de nascimento não pode ser maior que o ano atual.')
elif ano_nasc < 1900:
    print('Erro: O ano de nascimento parece inválido.')
else:
    idade = ano_atual - ano_nasc
    print(f'Sua idade é {idade} anos.')