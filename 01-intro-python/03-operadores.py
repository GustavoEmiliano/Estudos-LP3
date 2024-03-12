#Operadores aritméticos
# +, =, *, /, **

nota1 = 10
nota2 = 5.5
nota3 = 7

media = (nota1 + nota2 +  nota3)/3
 
 
# numero elevado a outro
# e elevado n
# 10 elevado a 2

numbero = 10
numero_elevado_2 = numbero * numbero
numero_elevado_2 = numbero ** 2

# operadores lógicos 
# and, or e not 

print(True and True)    #True
print(True and False)   #False
print(False and True)   #False
print(False and False)  #False

print(True or True)     #True
print(True or False)    #True
print(False or True)    #True
print(False or False)   #False

print (not True)        #False
print (not False)       #True 

# permitir entrada 
# quando o usuário for funcionário 
# quando o usuário não estiver bloqueando E
# quando hora atual estiver entre 8h e 18h 

# permiti entrada
# quando for admin

usuario_funcionario = True
usuario_bloqueado = False
hora_atual = 17
usuario_admin = False 

horario_comercial = hora_atual >=8 and hora_atual <= 18  # se for um valor válido, na condição do if, horario_comercial é substituida por True 
usuario_ativo = usuario_funcionario and not usuario_bloqueado

if usuario_admin or (usuario_ativo and horario_comercial):
    print("Acesso permitido")


idade = 22
maioridade = idade >= 18 # recebe um true ou um false dependendo da idade 

if maioridade: 
    pass


# operadores de comparação 
# ==, !=, >, <, >=, <=

idade = 25

maioridade = idade >= 18

if (media) >= 6:
    print("Aprovado")
    
    
# is, is not
# operador de identidade 
# comparar se os objetos ocupam o mesmo espaço de memória 

a = [1, 2, 3]
b = [1, 2, 3]

print (a == b)  # True 
print (a is not b)  #True 
print (a is b) #False  


# operador in e not in
# verifica se o elemento existe ou não em uma sequÊncia 
# str, list, tuple 

opcoes = ('sim', 'não', 'nao', 'talvez')
opcao = input('Digite uma opção ')  # "     SIM      "
opcao = opcao.lower().strip()       # "     sim      " e depois # "sim"

if opcao in opcoes: 
    print('ok')
else:
    print('Não existe essa opção')

# PARA O PROBLEMA DO NÃO SEM ACENTO, COLOQUEI A VARIAÇÃO nao NA TUPLA

numeros = {1,2,3,5,6}
for x in numeros:
    print(x)