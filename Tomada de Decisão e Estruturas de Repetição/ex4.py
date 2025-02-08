# 4. Implemente um programa que classifique um aluno com base em sua
# pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se
# a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é
# reprovado.

# Solicita a nota ao usuário
nota = int(input('Digite sua pontuação no exame:'))

# Verifica se a nota está no intervalo válido
if 0 <= nota <= 10:
    # Verifica se o aluno foi aprovado ou reprovado
    if nota >= 7:
        print('Aprovado!')
    else:
        print('Reprovado!')
else:
    print('Nota inválida!')