import requests
import pandas as pd
import json

cidade = input("Digite o nome da cidade: ").capitalize()

geocoding = f"https://geocoding-api.open-meteo.com/v1/search?name={cidade}&count=10&language=en&format=json"


local = requests.get(geocoding)

dados = local.json()

#-------------Cria o arquivo Json para leitura mais fácil---------------

with open("Coordenadas.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)

#------------------------------------------------------------------------

latitude = dados["results"][0]["latitude"]
longitude = dados["results"][0]["longitude"]

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,precipitation,cloud_cover,wind_speed_10m,wind_direction_10m&timezone=America%2FSao_Paulo"
resposta = requests.get(url)

data = resposta.json()

#-------------Cria o arquivo Json para leitura mais fácil---------------

with open("dados_climaticos.json", "w", encoding="utf-8") as arquivo:
    json.dump(data, arquivo, indent=4, ensure_ascii=False)

#------------------------------------------------------------------------

clima = data["current"]

tabela = pd.DataFrame([clima])

tabela = tabela[["time", "temperature_2m", "wind_speed_10m", "wind_direction_10m", "relative_humidity_2m", "precipitation", "cloud_cover"]]

tabela = tabela.rename(columns={
    "time" : "Horário",
    "temperature_2m" : "Temperatura",
    "wind_speed_10m" : "Velocidade do vento",
    "wind_direction_10m" : "Direção do vento",
    "precipitation" : "Probabilidade de chuva",
    "relative_humidity_2m" : "Umidade",
    "cloud_cover" : "Cobertura de nuvens"

})

print(tabela.T)