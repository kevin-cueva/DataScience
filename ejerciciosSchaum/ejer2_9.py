import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from pyparsing import alphas

"""
Ejercicio 2.9 de Schaum edicion 4 
"""
def limite_inferior(start, intervalo_clsase, cantidad):
    start = start-1
    con = 0
    lista = []
    while con <cantidad:
        lista.append(start)
        start = start+intervalo_clsase
        con+=1
    return lista

def limite_superior(start, intervalo_clsase, cantidad):
    start = start + intervalo_clsase -2
    con = 0
    lista = []
    while con <cantidad:
        lista.append(start)
        start = start+intervalo_clsase
        con+=1
    return lista


matriz_estatura_estudiantes = np.array([[67, 70, 64, 67, 66, 67, 64, 66, 68, 64, 63, 67, 74, 59, 67],
                                        [74, 71, 70, 64, 69, 65, 62, 61, 66, 68, 61, 64, 65, 68, 67],
                                        [65, 66, 65, 64, 56, 65, 62, 65, 65, 63, 67, 66, 59, 69, 67]])

con1 = 0
new_array = np.sort(matriz_estatura_estudiantes.flatten())
for dato in new_array:
    if (dato >= 63 and dato <67):
        con1=con1+1
print(con1)
RANGO = 5
estatura_minima = np.amin(matriz_estatura_estudiantes)
estatura_maxima = np.amax(matriz_estatura_estudiantes)
rango = estatura_maxima - estatura_minima
intervalo_de_clase = round(rango/RANGO)
limites_inferiores = np.array(limite_inferior(estatura_minima,intervalo_de_clase,RANGO))
limites_superiores = np.array(limite_superior(estatura_minima,intervalo_de_clase,RANGO))
print(f'Estatura menor: {estatura_minima}')
print(intervalo_de_clase)
print(limites_inferiores)
print(limites_superiores)

#Metodo para calcular frecuendias de Numpy
frecuencias, extremos = np.histogram(matriz_estatura_estudiantes, bins=5)

#Intervalos para poder graficar
intervalo = np.append(limites_inferiores, limites_superiores[-1])
print(intervalo)
inicio = 55
fin = 74
ancho_de_bin = intervalo_de_clase
div = np.linspace(inicio, fin, round(1+(fin-inicio)/ancho_de_bin))
#Graficando con Matplolib}
plt.hist(new_array, intervalo)
plt.grid(color='r', linestyle='dotted', linewidth=1)
plt.show()