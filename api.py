import requests
import pandas as pd

def buscar_coordenadas(cidade):
   try:  
      geocoding = f"https://geocoding-api.open-meteo.com/v1/search?name={cidade}&count=10&language=en&format=json"

      local = requests.get(geocoding)
      dados = local.json()
      
      if "results" not in dados:
           return None

      latitude = dados["results"][0]["latitude"]
      longitude = dados["results"][0]["longitude"]

      return latitude, longitude, dados

   except requests.exceptions.RequestException:
      print("Conexão com API perdida.")


def buscar_dados(latitude, longitude):

   try:
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,precipitation,cloud_cover,wind_gusts_10m,wind_speed_10m,wind_direction_10m&timezone=America%2FSao_Paulo"
    resposta = requests.get(url)
    data = resposta.json()

    clima = data["current"]

    tabela = pd.DataFrame([clima])

    tabela = tabela[["time", "temperature_2m", "wind_gusts_10m","wind_speed_10m", "wind_direction_10m", "relative_humidity_2m", "precipitation", "cloud_cover"]]

    tabela = tabela.rename(columns={
    "time" : "Horário",
    "temperature_2m" : "Temperatura",
    "wind_speed_10m" : "Velocidade do vento",
    "wind_direction_10m" : "Direção do vento",
    "wind_gusts_10m" : "Rajadas de vento",
    "precipitation" : "Chuva",
    "relative_humidity_2m" : "Umidade",
    "cloud_cover" : "Cobertura de nuvens"})

    return tabela, clima, data
   except requests.exceptions.RequestException:
       print("Conexão com API perdida!!")