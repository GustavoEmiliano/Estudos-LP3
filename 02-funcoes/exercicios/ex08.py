#  Ex08 - Função de Contagem de Palavras:
# Escreva uma função que receba uma string (frase) como argumento e 
# retorne um dicionário onde as chaves são as palavras únicas no texto e os valores 
# são o número de vezes que cada palavra aparece no texto.
# Depois, teste a função com diferentes textos fornecidos pelo usuário.


def contar_palavras(texto):
    texto_limpo = texto.lower().replace(",", "").replace(".", "").replace(";", "").replace(":", "").replace("!", "").replace("?", "")
    palavras = texto_limpo.split()

    contagem_palavras = {}
    for palavra in palavras:
        if palavra in contagem_palavras:
            contagem_palavras[palavra] += 1
        else:
            contagem_palavras[palavra] = 1

    return contagem_palavras

while True:
    texto = input("Digite uma frase (ou digite 'exit' para encerrar): ")
    if texto.lower() == 'exit':
        break
    resultado = contar_palavras(texto)
    print("\nContagem de palavras:")
    for palavra, quantidade in resultado.items():
        print(f"'{palavra}': {quantidade}")
