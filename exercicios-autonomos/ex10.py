#Crie um programa em Python que pergunte ao usuário o
# preço de um produto e calcule seu valor com um desconto de 10%.

valorProduto = float(input("Digite o valor do produto que deseja comprar:"))
valorAtualizado = valorProduto - (valorProduto * 0.10)
print("O valor do produto com o desconto de 10% é: ", valorAtualizado)