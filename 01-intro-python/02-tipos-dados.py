# Tipos de dados
# int, float, String, char, list, 
# dict, None, tuple, set

# int 
idade = 20
temperatura = -30

# float
altura = 1.45
PI = 3.14

# string
nome = "Gabriel"
Nome = 'Gabriel'

print (nome[0])# acessando caracteres individualmente
print (nome[0:3])



# nome é um objeto da classe string
# nome tem o que? métodos e atributos, logo
# nome.métodos_disponíveis

nome.capitalize #apenas o retorno é com a primeira letra em maiúsculo
nome = nome.capitalize #neste caso, o valor guardado mudou

print (nome)


# char
letra = 'a'
letra = 'b'

# interpolação de string e variáveis
# f-string
nome = "João"
idade = 22

"""
mensagem = "Olá nome,você tem idade anos"
"""

mensagem = f"Olá {nome}, você tem {idade} anos"

print (mensagem)

# list
# lista de valores
# pode ser alterada

habilidades = ['java', 'css', 'c#']

print(habilidades)
habilidades[0] = 'javascript'

print(habilidades)

habilidades.append('HTML')

print(habilidades)

habilidades.insert(0, 'kotlin')

print(habilidades)

habilidades.insert(15, 'TESTE')  

print(habilidades)
print(habilidades[5])

# set
# não indexado
# não permite elementos duplicados 
# Digite a mensagem
# Digite os e-mails de destino
# maria@email.com
# joao@email.com
# maria@email.com

emails = {'maria@email.com', 'joao@email.com', 'maria@email.com'} #set usa chaves 

emails.add('maria@email.com')
print(emails)



# tuple
# "lista" de valores 
# não pode alterar, adicionar nem remover  ("lista constante")

opcoes = ('sim', 'não', 'talvez')

print(opcoes)

# for
for opcao in opcoes:
    print(opcao)

print("")

for habilidade in habilidades:
    print(habilidade)

# dict
# dicionário
# chave : valor
# key : value

# site de emprego

empresa = 'Google'
titulo = 'Engenheiro de software'
salario = 20000.00
remoto = False
# características de uma vaga

# dicionário
vaga = {
    'empresa' : 'Google',
    'titulo' : 'Engenheiro de software',
    'salario' : 200000.00,
    'remoto' : False
}

print(" ")
print(vaga['salario'])
print(" ")
print(vaga['empresa'])
print(" ")
print(vaga['titulo'])
print(" ")
print(vaga['remoto'])

# None

nome = None #apenas declara a variável, sem valor atribuído

"""
def gerar_boletim(prontuario):
    # se encontrou aluno no bdd
    return 'boletim'
    #else
    return None 

"""
