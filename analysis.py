def chuva(umidade, nuvens, precipitacao):
    if precipitacao > 0:
       return "Já está chovendo!!"
    elif umidade > 80 and nuvens > 85:
        return "Há alta chance de chuva!"
    elif umidade > 70 and nuvens > 60:
        return "Há possibilidade de chuva!"
    elif umidade < 40:
        return "Clima seco"
    else:
        return "Baixa chance de chuva"
    