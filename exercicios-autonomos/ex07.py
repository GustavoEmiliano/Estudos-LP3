#  Desenvolva um programa em Python que converta uma temperatura de Celsius para Fahrenheit.

# Solicita a temperatura em Celsius ao usuário
temperaturaCelsius = float(input("Informe a temperatura em Celsius:"))

# Converte a temperatura para Fahrenheit utilizando a fórmula F = 32 + (C * 1.8)
temperaturaFahrenheit = 32 + (temperaturaCelsius * 1.8)

# Exibe o resultado da conversão
print("A temperatura em Fahrenheit é:", temperaturaFahrenheit)
