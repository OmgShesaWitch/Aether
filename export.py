import json
import csv
import os

def exportarjson(nome_arquivo, dados):

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
      json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def exportarcsv(nome_arquivo, dados):
   campos = [
      "cidade",
      "data",
      "temperatura",
      "velocidade_vento",
      "rajadas_vento",
      "umidade",
      "precipitacao",
      "cobertura_nuvens",
   ]
  
   arquivo_existe = os.path.exists("weather_history.csv")

   with open(nome_arquivo, "a", newline="", encoding="utf-8") as arquivo:
      writer = csv.DictWriter(
         arquivo,
         fieldnames=campos
      )
      if not arquivo_existe:
         writer.writeheader()
      writer.writerow(dados)