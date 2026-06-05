def validar_cidade(entrada: str) -> str | None:
    entrada_limpa = entrada.strip()
    if not entrada_limpa:
        return "Por favor, digite o nome de uma cidade."
    if entrada_limpa.isdigit():
        return "Por favor, digite o nome da cidade."
    return None
