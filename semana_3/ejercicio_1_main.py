'''1- Elabore un módulo que contenga 3 funciones:
a- una función que calcule el área de un círculo. Utilizar parámetros opcionales para definir
que en caso de no recibir un radio el valor del mismo será 3.
b- una función que calcule el área de un cuadrado y reciba la longitud del lado como
parámetro, sin parámetros opcionales.
c- una función que calcule el área de un triángulo recibiendo base y altura por parámetro'''
import modulo_area 
import modulo_perimetro
print("-----------AREAS-------------------")
modulo_area.area_circulo (None)
modulo_area.area_cuadrado (2.6)
modulo_area.area_triangulo (5,9)
print("-----------PERIMETROS---------------")
modulo_perimetro.calcular_perimetro_circulo (10)
modulo_perimetro.calcular_perimetro_cuadrado (2)
modulo_perimetro.calcular_perimetro_triangulo (5)
