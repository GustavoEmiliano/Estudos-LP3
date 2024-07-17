import sys

def calculaIMC():
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    imc = peso / (altura ** 2)
    mensagem = 'O seu IMC é de: {:.1f}'.format(imc)
    
    if imc < 18.5:
        classificacao = 'Você está abaixo do peso normal'
    elif 18.5 <= imc < 24.9:
        classificacao = 'Você está na faixa de peso normal'
    elif 25 <= imc < 29.9:
        classificacao = 'Você está com sobrepeso'
    elif 30 <= imc < 34.9:
        classificacao = 'Você está com obesidade de classe 1'
    elif 35 <= imc < 39.9:
        classificacao = 'Você está com obesidade de classe 2'
    else:  # Para IMC >= 40
        classificacao = 'Você está com obesidade de classe 3'
        
    print(mensagem)
    print(classificacao)

def menuIMC():
    while True:
        print("\n----- CALCULADORA DE IMC -----")
        print("1. Calcular IMC")
        print("2. Sair")
        print("------------------------------")
        opc = int(input("Digite o número da opção desejada: "))

        if opc == 1:
            resultado = calculaIMC()
            print(resultado)
        elif opc == 2:
            print("Saindo da calculadora. Até logo!")
            sys.exit()
        else:
            print("Opção inválida. Por favor, tente novamente.")


