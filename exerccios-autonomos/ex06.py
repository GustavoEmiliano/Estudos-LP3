#  Crie um programa em Python que peça o nome e a idade de duas pessoas e informe qual delas é mais velha.
print("======================================")
idade1 = (input("Digite a idade de Janiely:"))
idade1 = int(idade1)
idade2= (input("Digite a idade de Gustavo:"))
idade2 = int(idade2)

if (idade1 > idade2):
    print("======================================")
    print("\n         Janiely é mais velha\n")
    print("======================================")
elif (idade1 < idade2):
    print("======================================")
    print("\n         Gustavo é mais velho\n")
    print("======================================")
elif (idade1 == idade2):
    print("======================================")
    print("\n     Os dois tem a mesma idade\n")
    print("======================================")