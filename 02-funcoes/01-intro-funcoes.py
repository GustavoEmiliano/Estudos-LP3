#Função

#Quero somar uma lista de numeros
#usar função sum():

#Quero calcular media de notas dos alunos
# 1. tem no python?
# 2. alguém ja progamou (copiar ou importar depenedencia)
# 3. declarar



# 1. Declaração
#def nome_função(parametro1,parametro2)
#    return valor


# 2. Chamada
print('Olá')
sum([1,3,3])

#Função sem retorno e sem parâmetros
def imprimir_mensagem():
    print("Socorro")

    
imprimir_mensagem()
imprimir_mensagem()

#Função sem retorno e com parâmetros
#parâmeros vs argumentos
def saudacoes(nome):
    print(f"Bom dia {nome}")

#argumento para parâmetro nome 'Maria'
saudacoes('Maria')

#argumento para parâmetro nome
nome_completo = 'José Da Silva'
saudacoes(nome_completo)


#Função com retorno e sem parâmetros
def obter_mensagem():
    return "Socorro!!!"

mensagem = obter_mensagem()
print(mensagem)

print(obter_mensagem())



#Função com retorno e com parâmetros
def gerar_saudacao(nome):
    return f"Bom dia {nome}"

print(gerar_saudacao("Gabriela"))

# retorno   parametros
#  nao         nao
#  nao         sim
#  sim         nao
#  sim         sim(adequado) (funçao pura)

# imprimir saudacao
#Saudacao = frase (dinamica) nome(nome)
# 'Bom dia Pedro'
# 'Boa tarde Maria'
# 'Boa noite Pedro'

def saudacao(frase, nome):
    print(f"{frase} {nome}")
    
saudacao("Te amo", "Gustavo")

def saudacao(frase, nome):
    return f"{frase} {nome}"

print(saudacao("Te amo", "GU"))
     

#Entrada
notas_alunos = [
    [10.0, 10.0, 7.0],
    [1.0, 1.0, 1.0],
    [3.0, 3.0, 3.0],  
]

def calcular_media(notas): #notas é uma lista
    return sum(notas)/len(notas) #soma dos valores dentro da lisata dividido pelo tamanho da lista NOTAS 

def calcular_media_alunos(notas_alunos):
    medias = [] #lista de medias 
    
    for notas in notas_alunos: #para cada lista de notas dentro da lisata de todas as notas...
        medias.append(calcular_media(notas)) #adiciona na lista a média de notas de cada lista de 3 valores
        
    return medias
    
print(calcular_media_alunos(notas_alunos))
    
  
    
    
    # Argumentos nomeados

def saudacao(nome, frase):
    return f"{frase}, {nome}"

#       vvvvvvv     vvvvv       argumentos posicionais
saudacao("Joao", "FAAALAAAA ")

saudacao(frase="tudo bem", nome="Davi")

# Valores padrão

def set_visivel(visivel=True):
    if visivel:
        print("Tudo está visivel agora")
    else:
        print("Tudo escuro...")


# Sobrecarga e sobrescrita
# Sobrecarga: não existe em python </3
# Sobrescrita: reescrita da função