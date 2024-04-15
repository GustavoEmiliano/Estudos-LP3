#  Ex07 - Jogo da Forca:
#  Implemente uma versão simples do jogo da forca. 
#  O programa começa com uma palavra oculta (o usuário não vê) e o usuário 
#  tenta adivinhar a palavra, letra por letra. 
#  O usuário tem um número limitado de tentativas para adivinhar toda a palavra.

print("Programa Forca")
import random

def escolher_palavra():
    palavras = ['computador', 'programacao', 'python', 'desenvolvimento', 'inteligencia', 'artificial', 'algoritmo']
    return random.choice(palavras).lower()

def exibir_palavra(palavra, letras_adivinhadas):
    exibicao = ''
    for letra in palavra:
        if letra.lower() in letras_adivinhadas or letra == ' ':
            exibicao += letra
        else:
            exibicao += '_'
    return exibicao

def desenhar_forca(erros):
    print("   _______     ")
    print("  |/      |    ")

    if erros >= 1:
        print("  |      (_)   ")
        if erros == 2:
            print("  |      \|    ")
        elif erros == 3:
            print("  |      \|/   ")
        elif erros >= 4:
            print("  |      \|/   ")
            print("  |       |    ")
        if erros == 5:
            print("  |       |    ")
        elif erros >= 6:
            print("  |       |    ")
            print("  |      /     ")
        if erros == 7:
            print("  |      / \   ")

    print("  |            ")
    print(" _|___         ")
    print()

def jogar_jogo():
    palavra_a_adivinhar = escolher_palavra()
    letras_adivinhadas = []
    tentativas_restantes = 7
    erros = 0

    print("Bem-vindo ao Jogo da Forca!")
    print(exibir_palavra(palavra_a_adivinhar, letras_adivinhadas))

    while True:
        desenhar_forca(erros)
        palpite = input("Digite uma letra: ").lower()

        if palpite in letras_adivinhadas:
            print("Você já tentou esta letra. Tente outra.")
        elif palpite in palavra_a_adivinhar:
            letras_adivinhadas.append(palpite)
            print(exibir_palavra(palavra_a_adivinhar, letras_adivinhadas))
            if '_' not in exibir_palavra(palavra_a_adivinhar, letras_adivinhadas):
                print("Parabéns! Você acertou a palavra:", palavra_a_adivinhar)
                break
        else:
            erros += 1
            tentativas_restantes -= 1
            print("Letra incorreta! Você tem {} tentativas restantes.".format(tentativas_restantes))
            if erros == 7:
                print("Você perdeu! A palavra correta era:", palavra_a_adivinhar)
                break

jogar_jogo()
