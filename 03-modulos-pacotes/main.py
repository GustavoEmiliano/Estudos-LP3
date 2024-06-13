#importa tudo de matematica 
import matematica

print(matematica.PI)
print(matematica.somar(10.0, 3.0))
print(matematica.subtrair(10.0, 4.0))
print("-------------------------------------------")


#importar apenas os elemetnos (constantes, funcoes, classes)
#necessarios
from matematica import PI, subtrair, somar


print(PI)
print(somar(10.0, 3.0))
print(subtrair(10.0, 4.0))
print("-------------------------------------------")
#caso tenha conflito de nome
from matematica import PI as PI_MAT
PI = 999999
print(PI)
print(PI_MAT)
print(somar(10.0, 3.0))
print(subtrair(10.0, 4.0))
print("-------------------------------------------")
print("A partir daqui começa módulos e pacotes:")

#importar a função media do pacote estatistica e módulo descritiva

from estatisticas.descritiva import media
from estatisticas.inferencial import VALOR


