'''
Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
'''


def area(radio):
    """
    Funcion que calcula el area de un circulo.
    :parameter
    radio: Radio del circulo
    :return: Area de circulo de radio
    """
    pi = 3.1415
    return 2*pi*radio**2


def volumen(radio, altura):
    """
    Función que calcula el volumen de un cilindro.
    :parameter
    radio: Es el radio de la base del cilindro.
    altura: Es la altura del cilindro.
    Devuelve el volumen del clindro de radio y altura.
    """
    return area(radio)*altura

print(volumen(3,5))