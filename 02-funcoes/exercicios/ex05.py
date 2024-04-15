# Ex05 - Verificador de Palíndromos: 
# Solicite ao usuário que digite uma palavra ou frase e 
# verifique se é um palíndromo (ou seja, pode ser lida de frente para trás e de trás para frente da mesma forma).

print("Verificador de Palindromos")

def verifica_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]

texto = input("Digite uma palavra ou frase: ")
if verifica_palindromo(texto):
    print(texto + " é um palíndromo")
else:
    print(texto + " não é um palíndromo")