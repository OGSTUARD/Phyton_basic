def decimal_a_binario(decimal):
    """Convierte un número decimal en binario"""
    if decimal == 0:
        return '0'
    binario = ''
    while decimal > 0:
        resto = decimal % 2
        binario = str(resto) + binario
        decimal = decimal // 2
    return binario

def binario_a_decimal(binario):
    """Convierte un número binario en decimal"""
    decimal = 0
    potencia = 0
    for digito in reversed(binario):
        decimal += int(digito) * (2 ** potencia)
        potencia += 1
    return decimal


