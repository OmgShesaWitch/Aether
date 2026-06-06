import json

def exportarjson(nome_arquivo, dados):

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
      json.dump(dados, arquivo, indent=4, ensure_ascii=False)
