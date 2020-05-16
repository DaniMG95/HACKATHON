'''
    Escribir un programa que pida al usuario un número entero y muestre por pantalla un 
    triángulo rectángulo como el de más abajo, de altura el número introducido.

    *
    **
    ***
    ****
    *****
'''

n=int(input("Numero : "))

for i in range(n):
    valor="*"
    for j in range(i):
        valor=valor+"*"
    print(valor)