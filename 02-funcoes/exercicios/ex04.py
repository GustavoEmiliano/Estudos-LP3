#  Ex04 - Simulador de Eleições:
# Crie um programa que simule uma votação com três candidatos. 
# O programa deve pedir ao usuário para votar várias vezes e, no final,
# mostrar o número de votos de cada candidato e quem foi o vencedor.

def votar(candidatos, numero_votos):
    while numero_votos > 0: 
        voto = input("Digite o número do candidato em quem deseja votar (1, 2 ou 3): ")

        if voto == '1':
            candidatos[0] += 1
            numero_votos -= 1
        elif voto == '2':
            candidatos[1] += 1
            numero_votos -= 1
        elif voto == '3':
            candidatos[2] += 1
            numero_votos -= 1
        else:
            print("Voto inválido. Digite 1, 2 ou 3 para votar nos candidatos.")

def mostrar_resultados(candidatos):
    print("\nVotos no candidato 1 =", candidatos[0])
    print("Votos no candidato 2 =", candidatos[1])
    print("Votos no candidato 3 =", candidatos[2])

    if candidatos[0] > candidatos[1] and candidatos[0] > candidatos[2]:
        print("Candidato 1 é o vencedor!")
    elif candidatos[1] > candidatos[0] and candidatos[1] > candidatos[2]:
        print("Candidato 2 é o vencedor!")
    elif candidatos[2] > candidatos[0] and candidatos[2] > candidatos[1]:
        print("Candidato 3 é o vencedor!")
    else:
        print("Houve um empate.")

def simulador_eleicao():
    print("Programa Eleição")
    candidatos = [0, 0, 0]
    numero_votos = int(input("Digite o número de votos desejado: "))
    
    votar(candidatos, numero_votos)
    mostrar_resultados(candidatos)

simulador_eleicao()
