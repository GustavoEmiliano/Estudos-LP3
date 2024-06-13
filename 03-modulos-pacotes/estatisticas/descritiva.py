#funções dentro do módulo descritiva, dentro do pacote estatisticas
from .inferencial import VALOR   # um ponto = diretório atual
from ..matematica import somar   # dois pontos = diretório anterior ao atual


def media(valores):
    return (sum(valores)/len(valores))

def minimo(valores):
    return (min(valores))

def maximo(valores):
    return (max(valores))

def minhafuncao():
    print(VALOR)