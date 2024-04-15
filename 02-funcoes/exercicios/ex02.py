#  Ex02 - Tabuada de Um Número: 
# Solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.

print("\n=========")
print("|TABUADA|")
print("=========")

numero = int(input("Entre com um numero:"))

def exibeTabuada(numero):
    contador = 1

    while contador <= 10:
        print (numero * contador)
        contador +=1
        
exibeTabuada(numero)