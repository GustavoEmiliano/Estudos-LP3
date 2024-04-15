## Ex01 - Jogo de Adivinhação: 
#  Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente.
# Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número.

import random

numeroInserido = int(input("Digite o seu numero palpite:"))
numeroAleatorio = random.randint(1, 100)

def verificaPalpite(numeroInserido, numeroAleatorio):

    
    while(numeroAleatorio is not numeroInserido):
        if (numeroInserido > numeroAleatorio):
            print("O plapite está alto")
            numeroInserido = float(input("Insira outro número: "))   
        elif (numeroInserido < numeroAleatorio):
            print("O plapite está baixo")
            numeroInserido= float(input("Insira outro número: "))   
        else:
            print("Acertou")
            break

verificaPalpite(numeroInserido, numeroAleatorio)








