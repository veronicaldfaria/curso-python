# 6. Crie um programa que solicite ao usuário um login e uma senha. O
# programa deve permitir o acesso apenas se o usuário for "admin" e a senha
# for "admin123", caso contrário imprima uma mensagem de erro.

import getpass

login = input('Digite o login:')  
senha = getpass.getpass('Digite a senha:')  # Isso oculta a senha enquanto o usuário digita

if login == 'admin' and senha == 'admin123':
    print('Acesso permitido!')
else:
    print('Acesso negado.')