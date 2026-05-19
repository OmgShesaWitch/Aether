def cidadenaoencontrada():
    return "Cidade não encontrada!"

def inputinvalido(entrada):
    if entrada.strip() == "":
        return "Por favor, digite o nome de uma cidade."
    if entrada.isdigit() == True:
        return "Por favor, digite o nome da cidade."
