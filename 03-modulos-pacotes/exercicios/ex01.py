# Ex01. Crie um programa que recebe como entrada o comprimento, altura e a largura de um aquário e calcule as seguintes informações.

# O volume do aquário em litros;
# A potência do termostato necessária para manter a temperatura adequada dentro do aquário;
# A quantidade em litros de filtragem por hora necessária para manter a qualidade da água.
# Volume é dado por (comprimento * altura * largura) / 1000
# A potência do termostato depende do tamanho do aquário e da temperatura ambiente. Para o cálculo utilizar a fórmula:
# potencia = volume * 0,05 * (temperatura desejada - temperatura ambiente)
# A quantidade de filtragem por hora deve ser no mínimo 2 a 3 vezes o volume do aquário.

from functions_aquario import calc_vol, calc_potencia, calc_filtragem

def exibir_menu():
    print("\n===============================")
    print("        Menu do Aquário        ")
    print("===============================")
    print("1 - Calcular volume do aquário")
    print("2 - Calcular potência do termostato")
    print("3 - Calcular capacidade de filtragem")
    print("0 - Sair")
    print("===============================")

while True:
    exibir_menu()
    opcao = input("\nEscolha uma opção: ")

    if opcao == '1':
        comprimento = float(input("Digite o valor para o comprimento do aquário (cm): "))
        altura = float(input("Digite o valor para a altura do aquário (cm): "))
        largura = float(input("Digite o valor para a largura do aquário (cm): "))
        volume = calc_vol(comprimento, altura, largura)
        print(f"\nVolume do aquário: {volume:.2f} litros")
    elif opcao == '2':
        comprimento = float(input("Digite o valor para o comprimento do aquário (cm): "))
        altura = float(input("Digite o valor para a altura do aquário (cm): "))
        largura = float(input("Digite o valor para a largura do aquário (cm): "))
        volume = calc_vol(comprimento, altura, largura)
        temp_desejada = float(input("Qual é a temperatura desejada para o aquário (°C)? "))
        temp_ambiente = float(input("Qual é a temperatura atual do ambiente (°C)? "))
        potencia = calc_potencia(volume, temp_desejada, temp_ambiente)
        print(f"\nPotência do termostato necessária: {potencia:.2f} Watts")
    elif opcao == '3':
        comprimento = float(input("Digite o valor para o comprimento do aquário (cm): "))
        altura = float(input("Digite o valor para a altura do aquário (cm): "))
        largura = float(input("Digite o valor para a largura do aquário (cm): "))
        volume = calc_vol(comprimento, altura, largura)
        filtragem_minima, filtragem_maxima = calc_filtragem(volume)
        print(f"\nCapacidade de filtragem necessária:")
        print(f"Mínima: {filtragem_minima:.2f} litros por hora")
        print(f"Máxima: {filtragem_maxima:.2f} litros por hora")
    elif opcao == '0':
        print("\nSaindo...")
        break
    else:
        print("\nOpção inválida. Tente novamente.")