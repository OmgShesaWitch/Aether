import requests
import pandas as pd

url = "https://api.open-meteo.com/v1/forecast?latitude=-22.90&longitude=-43.20&current=temperature_2m,wind_speed_10m,wind_direction_10m&timezone=America%2FSao_Paulo"

resposta = requests.get(url)

data = resposta.json()

clima = data["current"]

tabela = pd.DataFrame([clima])

tabela = tabela[["time", "temperature_2m", "wind_speed_10m", "wind_direction_10m"]]

tabela = tabela.rename(columns={
    "time" : "Horário",
    "temperature_2m" : "Temperatura",
    "wind_speed_10m" : "Velocidade do vento",
    "wind_direction_10m" : "Direção do vento"
})

print(tabela)
print(data["timezone"])