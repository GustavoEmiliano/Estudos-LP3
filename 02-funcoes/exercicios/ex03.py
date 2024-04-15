#  Ex03 - Contador de Vogais e Consoantes: 
# Peça ao usuário para digitar uma frase e retorne o número de vogais e consoantes na frase.

print("Programa Calcula Vogais e Consoantes")
frase = input("Digite uma frase:")

def contar_vogais_consoantes(frase):
    vogais = ['a', 'e', 'i', 'o', 'u']
    num_vogais = 0
    num_consoantes = 0
    
    for letra in frase.lower():
        if letra.isalpha():
            if letra not in vogais:
                num_consoantes += 1
            else:
                num_vogais += 1

    return num_vogais, num_consoantes
    
vogais, consoantes = contar_vogais_consoantes(frase)

print(f"Na frase '{frase}' temos {vogais} vogais e {consoantes} consoantes.")