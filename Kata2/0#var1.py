'''
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
Escribe un programa que comience leyendo el número de barras vendidas que no son del día. Después tu 
programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser 
fresca y el coste final total. 
'''

coste=3.49
descuento=1-0.6
precio_descuento=coste*descuento

numero_pan=int(input("Introduce el numero de barras vendidas:"))

print("El precio habitual es : "+str(coste))
print("El descuento es de :"+str(precio_descuento))
print("El precio final es : "+str(numero_pan*precio_descuento))