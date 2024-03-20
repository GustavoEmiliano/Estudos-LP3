#Faça um programa em Python que solicite o raio de um círculo e calcule sua área.
import math
print('==============================')
raio = float(input('Insira o valor do raio do círculo:'))
area = math.pi * (raio ** 2)
print('==============================')
print(f"A área do círculo é: {area}")
print('==============================')