"""
Ejercicio 2.2 del libro estaistica de Schaum 4 edicion
"""

import numpy as np
matriz_calificaciones = np.array([[68, 84, 75, 82, 68, 90, 62, 88, 76, 93],
                                  [73, 79, 88, 73, 60, 93, 71, 59, 85, 75],
                                  [61, 65, 75, 87, 74, 62, 95, 78, 63, 72],
                                  [66, 78, 82, 75, 94, 77, 69, 74, 68, 60],
                                  [96, 78, 89, 61, 75, 95, 60, 79, 83, 71],
                                  [79, 62, 67, 97, 78, 85, 76, 65, 71, 75],
                                  [65, 80, 73, 57, 88, 78, 62, 76, 53, 74],
                                  [86, 67, 73, 81, 72, 63, 76, 75, 85, 77]])
size_matris = matriz_calificaciones.shape #Filas y columnas de la matriz
filas = size_matris[0]
columnas = size_matris[1]
print(matriz_calificaciones.ndim) # Numero de dimenciones
print(matriz_calificaciones.size) #Numero de elementos de la matriz o cantidad
calificacion_mas_alta = np.amax(matriz_calificaciones)
calificacion_mas_baja = np.amin(matriz_calificaciones)
rango = calificacion_mas_alta - calificacion_mas_baja
new_array = np.sort(matriz_calificaciones.flatten())[::-1] #flatten convierte la matriz en una array de una dimencion
con_est_75 = 0
con_est_85 = 0
con_est_65_y_85 = 0
for i in new_array:
    if (i>=75):
        con_est_75 = con_est_75+1
    if(i<85):
        con_est_85 = con_est_85+1
    if(i>65 and i<=85):
        con_est_65_y_85 = con_est_65_y_85+1

print(f'Calificacion mas alta: {calificacion_mas_alta}')
print(f'Califiacion mas baja: {calificacion_mas_baja}')
print(f'Rango: {rango}')
print(f'Las cinco calificaciones mas altas: {new_array[:5]}')
print(f'Las cinco calificaciones mas bajas: {new_array[-5:][::-1]}')
print(f'calificacion en el decimo lugar: {new_array[9]}')
print(f'La cantidad de estudiantes que obtuvieron 75 o más es: {con_est_75}')
print(f'La cantidad de estudiantes que obtuvieron menos de 85 es: {con_est_85}')
print(f'El porcentaje de estudiantes que obtuvieron calificaciones mayores a 65 pero no mayores a 85 es: {((con_est_65_y_85/80)*100):.2f} %')
