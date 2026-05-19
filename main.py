from api import buscar_coordenadas, buscar_dados
from analysis import chuva
from ErrorTreatment import inputinvalido



while True:

    cidade = input("Digite o nome da cidade: ").capitalize()

    if cidade == "0":
        break

    erro = inputinvalido(cidade)
    
    if erro:
        print(erro)
        cidade = input("Digite o nome da cidade: ").capitalize()

    resultado = buscar_coordenadas(cidade)

    if resultado is None:
        exit()

    latitude, longitude, dados = resultado

    tabela, clima, data = buscar_dados(latitude, longitude)

    previsao = chuva(clima["relative_humidity_2m"], clima["cloud_cover"], clima["precipitation"])

    print("--------------Previsão-------------- \n     ", previsao)

    horario = clima["time"]
    temperatura = clima["temperature_2m"]
    windspeed = clima["wind_speed_10m"]
    dirvento = clima["wind_direction_10m"]
    umidade = clima["relative_humidity_2m"]
    probchuva = clima["precipitation"]
    cloudcover = clima["cloud_cover"]

    print(("Horário: "), horario.replace("T", " "))
    print(("Temperatura: "),temperatura, "°C")
    print(("Velocidade do vento: "),windspeed, "km/h")
    print(("Direção do vento: "),dirvento, "°")
    print(("Umidade: "),umidade, "%")
    print(("Chuva: "),probchuva, "%")
    print(("Cobertura de nuvens: "),cloudcover, "%")