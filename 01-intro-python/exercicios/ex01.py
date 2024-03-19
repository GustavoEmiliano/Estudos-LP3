# ex01 - Escreva um programa em python que solicita ao usuário um número inteiro
# e apresente seu sucessor e antecessor

numero = input('Digite um número inteiro:')
#numero ainda é string nesse caso


numero = int(numero)

print(numero)

antecessor = numero - 1
sucessor = numero + 1
print("O seu antecessor é: ", antecessor)
print("O seu sucessor é: ", sucessor)