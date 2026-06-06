from api import buscar_coordenadas, buscar_dados
from analysis import analisar_chuva, avisos
from validacoes import validar_cidade
from export import exportarjson, exportarcsv
from urllib.parse import quote

while True:

    cidade = input("Digite o nome da cidade ou 0 para encerrar o programa: ").capitalize()
    cidadeformatada = quote(cidade)

    if cidade == "0":
        print("Programa encerrado...")
        break

    erro = validar_cidade(cidade)
    
    if erro:
        print(erro)
        continue

    resultado = buscar_coordenadas(cidadeformatada)

    if resultado is None:
        print("Cidade não encontrada ou erro na busca!")
        continue

    latitude, longitude, dados = resultado

    tabela, clima, data = buscar_dados(latitude, longitude)

    previsao = analisar_chuva(clima["relative_humidity_2m"], clima["cloud_cover"], clima["precipitation"])

    print("--------------Previsão-------------- \n     ", previsao)

    horario = clima["time"]
    temperatura = clima["temperature_2m"]
    velocidadevento = clima["wind_speed_10m"]
    dirvento = clima["wind_direction_10m"]
    umidade = clima["relative_humidity_2m"]
    precipitacao = clima["precipitation"]
    nuvens = clima["cloud_cover"]
    rajadas = clima["wind_gusts_10m"]
     
    
    dados_csv = {
       "cidade" : cidade,
       "data": horario,
       "temperatura": temperatura,
       "velocidade_vento": velocidadevento,
       "rajadas_vento": rajadas,
       "umidade": umidade,
       "precipitacao": precipitacao,
       "cobertura_nuvens": nuvens,
    }

    print(("Horário: "), horario.replace("T", " "))
    print(("Temperatura: "),temperatura, "°C")
    print(("Velocidade do vento: "),velocidadevento, "km/h")
    print(("Direção do vento: "),dirvento, "°")
    print(("Umidade: "),umidade, "%")
    print(("Chuva: "),precipitacao, "%")
    print(("Cobertura de nuvens: "),nuvens, "%")
    print("Rajadas de vento: ", rajadas, "km/h")

    avisosextras = avisos(clima["wind_gusts_10m"], clima["relative_humidity_2m"])

    if avisosextras != None:
       for aviso in avisosextras:
           print(aviso)

    exportarjson(f"{cidade}.json", data) 
    exportarcsv("weather_history.csv", dados_csv)