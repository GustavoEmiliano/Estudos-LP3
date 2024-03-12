# if 
# if consição
#   codigo 
#   codigo  

idade = 80
if idade >=18:
    print("maior de idade")
    
    
#if/else

if idade >=18:
    print("maior de idade")
else:
    print("menor de idade")

# if/elif/else

if idade >0 and idade <= 12:
    print("criança")
elif idade <= 17:
    print("adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")

#Condições aninhadas
email = "admin@gmail.com"
senha = "123"

if email == "admin@gmail.com":
    if senha == "123":
        print("liberado")
    else:
        print("erro")       
else:
    print("erro")
    
    if email == "admin@gmail.com" and senha == "123":
        print("liberado")
    else:
        print("erro")

#Entrada, email, senha
#Saida True ou Dalse

def liberar_acesso(email, senha):
    if email == "admin@gmail.com" and senha == "123":
        return True
    else:
        return False
    
    
def liberar_acesso(email, senha):
    return email == "admin@gmail.com" and senha == "123"

#Entrada hora_atual
#sim ou não
def horario_comercial(hora_atual):
    return hora_atual >=8 and hora_atual<=18

#dia              1,2,3,4,5,6,7
#palavra domingo, segunda, terça, quarta, quinta, sexta, sabado

dia = 7

if dia == 1:
    print("domingo")
elif dia == 2:
    print("segunda")

#lista = ["domingo", 'segunda', 'terça']
#dia = dia - 1
#print(lista(dia))


dias = {
    1: "domingo",
    2: "segunda",
    3: "terça",
    4: "quarta",
    5: "quinta",
    6: "sexta",
    7: "sabado",
}

if dia in dias:
    print(dias[dia])