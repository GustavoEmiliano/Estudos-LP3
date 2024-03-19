# for
palavra = "Python"
for letra in palavra:
    print(letra)

numeros = [1,2,3,4,5,6,8]
for numero in numeros:
    print(numero)

#range
#range(5) - 0,1,2,3,4

#range(start,stop)
#range(4,10) - 4,5,6,7,8,9

#range(start,stop,step)
#range(3,10,2) - 3,5,7,9


for i in range(10,101, 2):
    print(i)


#while

contador = 4
while contador < 5:
    print(contador)
    contador += 1 

#break
#break pula o loop
#encontrar o primeiro numero par

numeros = [-3,-2,0,1,2,3,4,5,6]
for numero in numeros:
    if numero % 2 == 0:
        print(numero)
        break
 

#continue 
#pula a iteração
for numero in numeros:
    if numero <= 0:
        continue
    print("é :",numero)
    
for numero in numeros:
    if numero >0:
        print("é :", numero)

#compreensão de lista 
numeros = [2,3,4]
quadrados = []
for numero in numeros:
    quadrados.append(numero ** 2)
 
print("quadrados: ", quadrados) 

cubos = [numero **3 for numero in numeros]  # se for alguma operação fica no começo 
print("cubos: ", cubos)
    
numeros = [1,2,3,4,5,6]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
        
print("pares: ", pares)

impares = [numero for numero in numeros if not numero % 2 == 0]  # se for condição fica no final, retorno é um booleano 

print("impares: ", impares)

palavras = ["Gabriel", "Luna", "MaiA"]
palavra2 = [palavra.upper() for palavra in palavras]
print(palavra2)