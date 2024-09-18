'''a- una función que calcule el área de un círculo. Utilizar parámetros opcionales para definir
que en caso de no recibir un radio el valor del mismo será 3.'''
#----------------funciones de areas----------------------------- (punto 1)
import math
def area_circulo (radio : float) -> float:
    valor_pi = math.pi  #importe el modulo math para sacar el valor de pi
    if radio == 0 or radio == None:  #pregunto si el radio es igual a 0 o nulo si se salteo
        radio = 3
    radio_al_cuadrado = radio ** 2
    area_del_circulo = valor_pi * radio_al_cuadrado
    return print (f"el area del circulo 1 es : {area_del_circulo}")

'''b- una función que calcule el área de un cuadrado y reciba la longitud del lado como
parámetro, sin parámetros opcionales.'''

def area_cuadrado (lado : float) -> float:
    area_del_cuadrado = lado * lado
    return print (f"el area del cuadrado 2 es : {area_del_cuadrado}")
    

'''c- una función que calcule el área de un triángulo recibiendo base y altura por parámetro'''
def area_triangulo (base : float, altura : float) -> float:
    area_del_triangulo = (base * altura) / 2
    return print (f"el area del triangulo 3 es : {area_del_triangulo}")


