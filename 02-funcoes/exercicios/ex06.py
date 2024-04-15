#  Ex06 - Conversor de Notas Escolares:
# Baseado em uma pontuação fornecida pelo usuário (0 a 100), 
# converta para o sistema de notas A, B, C, D, ou F, seguindo os padrões de conversão comuns.

print("Programa Conversor de Notas Escolares")
nota = float(input("Entre com a nota de 0 a 100: "))
def programa_notas_escolares(nota):
    if nota < 0 or nota > 100:
        print("Ops! Essa nota não vale. Escolha uma de 0 a 100, por favor")
    else:
        if nota < 20:
            print("Nota F")
        elif nota < 30:
            print("Nota D-")
        elif nota < 40:
            print("Nota D")
        elif nota < 45:
            print("Nota D+")
        elif nota < 50:
            print("Nota C-")
        elif nota < 60:
            print("Nota C")
        elif nota < 65:
            print("Nota C+")
        elif nota < 70:
            print("Nota B-")
        elif nota < 80:
            print("Nota B")
        elif nota < 85:
            print("Nota B+")
        elif nota < 90:
            print("Nota A-")
        elif nota < 100:
            print("Nota A")
        else:
            print("Nota A+")
            
programa_notas_escolares(nota)

