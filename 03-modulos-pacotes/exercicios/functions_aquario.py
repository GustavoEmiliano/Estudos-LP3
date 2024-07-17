def calc_vol(comprimento, altura, largura):
    volume = (comprimento * altura * largura) / 1000
    return volume

def calc_potencia(volume):
    temp_desejada = float(input("Qual é a temperatura desejada para o aquário (°C)? "))
    temp_ambiente = float(input("Qual é a temperatura atual do ambiente (°C)? "))
    potencia = volume * 0.05 * (temp_desejada - temp_ambiente)
    return potencia

def calc_filtragem(volume):
    filtragem_minima = volume * 2
    filtragem_maxima = volume * 3
    return filtragem_minima, filtragem_maxima