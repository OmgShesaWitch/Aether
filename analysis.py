def analisar_chuva(umidade, nuvens, precipitacao):
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
    
def avisos(velvento, umidade):
    if velvento >= 30:
        print("Parece que o vento está relativamente forte. Contraindicado sair de casa.")
    elif velvento >= 50:
        print("O vento está forte. Veículos altos, ciclistas e embarcações não devem sair.")
    elif velvento > 70:
        print("O vento está muito forte!!! Abrigue-se imediatamente.")
    if umidade <= 30 and umidade > 13:
        print("A umidade está baixa. Mantenha-se hidratado.")
    elif umidade <= 13:
        print("O clima está extremamente seco! Beba água e mantenha-se atento a sua saúde!!!") 