#Escreva um programa em Python que pergunte ao usuário sua idade e indique se ele é
#maior de idade ou não.

idade = input("Digite a sua idade:")
idade = int(idade)
if idade < 18:
    print("Você é menor de idade")
else:
    print("Você é maior de idade")