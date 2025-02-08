# 6. Vamos construir um jogo de forca. O programa escolherá
# aleatoriamente uma palavra secreta de uma lista predefinida. A palavra
# secreta será representada por espaços em branco, um para cada letra
# da palavra. O jogador terá um número limitado de 6 tentativas. Em cada
# tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente
# na palavra secreta, ela será revelada nas posições correspondentes. Se
# a letra não estiver na palavra, uma mensagem de erro deverá ser
# informada. Após um número máximo de erros, o jogador perde. O jogo
# continua até que o jogador adivinhe a palavra ou exceda o número
# máximo de tentativas.
# Dica: Você precisará importar uma biblioteca para resolver esse
# exercício

import random

# Lista de palavras para o jogo
palavras = ["python", "programacao", "computador", "inteligencia", "desenvolvimento"]

# Escolhe aleatoriamente uma palavra da lista
palavra_secreta = random.choice(palavras)
letras_descobertas = ["_"] * len(palavra_secreta)  # Exibe a palavra como "_ _ _"
tentativas_restantes = 6
letras_erradas = []

print("Bem-vindo ao jogo da Forca! 🎮")
print("A palavra tem", len(palavra_secreta), "letras.")
print(" ".join(letras_descobertas))

# Loop do jogo
while "_" in letras_descobertas and tentativas_restantes > 0:
    letra = input("\nDigite uma letra: ").lower()

    if letra in palavra_secreta:
        for i, l in enumerate(palavra_secreta):
            if l == letra:
                letras_descobertas[i] = letra
    else:
        if letra not in letras_erradas:
            letras_erradas.append(letra)
            tentativas_restantes -= 1
            print(f"Letra incorreta! Você tem {tentativas_restantes} tentativas restantes.")
        else:
            print("Você já tentou essa letra antes.")

    print("Palavra: ", " ".join(letras_descobertas))
    print("Letras erradas:", ", ".join(letras_erradas))

# Resultado do jogo
if "_" not in letras_descobertas:
    print("\nParabéns! Você adivinhou a palavra:", palavra_secreta.upper())
else:
    print("\nVocê perdeu! A palavra era:", palavra_secreta.upper())