import math 
#----------------funciones de perimetros-------------------------- (punto 2)
'''Elaborar un módulo que contenga 3 funciones. Pero este deberá calcular los perímetros
de las mismas figuras que el punto 1.'''

def calcular_perimetro_circulo (diametro : float) -> float:  #perimetro del circulo
    valor_de_pi = math.pi
    perimetro_del_circulo = valor_de_pi * diametro
    return print (f"el perimetro del circulo 1 es : {perimetro_del_circulo}")

def calcular_perimetro_cuadrado (lado : float)-> float:  #perimetro del cuadrado
    perimetro_del_cuadrado = lado * 4   # sumamos los 4 lados del cuadrado
    return print (f"el perimetro del cuadrado 2 es : {perimetro_del_cuadrado}")

def calcular_perimetro_triangulo (lado_triangulo : float ) -> float:   #perimetro  del triangulo
    perimetro_del_triangulo = lado_triangulo * 3  # sumo los 3 lados del triangulo
    return print (f"el perimetro del triangulo 3 es : {perimetro_del_triangulo}")
