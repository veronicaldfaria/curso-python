# 2. Faça um Programa que pergunte em que turno você estuda. Peça para
# digitar M-matutino, V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
# Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

# Solicita o turno ao usuário
turno = input('Em que turno você estuda (M-matutino, V-Vespertino ou N-Noturno)? ').upper()

# Verifica o turno e exibe a mensagem correspondente
if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Valor Inválido!')