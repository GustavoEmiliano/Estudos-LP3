# ex03- Crie um programa em python que recebe como entrada o valor
# de uma compra e apresente como saída o valor final com desconto e o 
#desconto aplicado com base nas seguintes regras:

# - compras entre R$0,01 e R$9,99 - 0% de descontos
# - compras entre R$10,00 e R$99,99 - 5% de descontos
# - compras entre R$100,00 e R$499,99 - 10% de descontos
# - compras iguais ou superiores a R$500,00 - 15% de desconto

valor = input("Digite o valor de sua compra: ")
valor = float(valor)

if valor >= 0 and valor < 10:
    print("Você não tem desconto, valor final: ", valor)
elif valor < 100:
    valorDesconto = valor - (valor * 0.05)
    print("Você tem 5% de desconto, valor final: ", valorDesconto)
elif valor < 500:
    valorDesconto = valor - (valor * 0.1)
    print("Você tem 10% de desconto, valor final: ", valorDesconto)
else:
    valorDesconto = valor - (valor * 0.15)
    print("Você tem 15% de desconto, valor final: ", valorDesconto)