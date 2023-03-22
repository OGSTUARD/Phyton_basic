def calcular_total_con_iva(cantidad_sin_iva, porcentaje_iva=21):
    """
    Función que calcula el total de una factura después de aplicar el IVA.

    :param cantidad_sin_iva: la cantidad sin IVA de la factura.
    :param porcentaje_iva: el porcentaje de IVA a aplicar (21% por defecto).
    :return: el total de la factura con IVA.
    """
    total = cantidad_sin_iva * (1 + porcentaje_iva / 100)
    return total
# Calcula el total de una factura con IVA al 21%
total_factura = calcular_total_con_iva(100)
print("El total de la factura es:", total_factura)

# Calcula el total de una factura con IVA al 10%
total_factura = calcular_total_con_iva(100, 10)
print("El total de la factura es:", total_factura)
