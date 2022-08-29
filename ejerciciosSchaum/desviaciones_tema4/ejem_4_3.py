#Encontrar la desviación media de los conjuntos de números
import numpy as np
import math
def desviacion_medi(lista:list, media:float)->float:
    res= 0.0
    tam = lista.size
    for i in lista:
        dato = abs(i-media)
        res = dato+res
    return res/tam
def desviacion_estandar(lista:list, media:float)->float:
    res= 0.0
    tam = lista.size
    for i in lista:
        dato = (i-media)**2
        res = dato+res
    return math.sqrt(res/tam)
from ctypes.wintypes import PINT

datos = np.array([12, 6, 7, 3, 15, 10, 18, 5])
#Paso 1: encontrar la media
media = np.sum(datos)/datos.size #Con logica 
media_numpy = datos.mean() #Con la libreria de numpy- la desviacion media
print(f'Desviacion media -> x = {desviacion_medi(datos,media)}') #con logica
print(f'Desviacion estandar -> s = {datos.std()}') #Con numpy
print(desviacion_estandar(datos,media)) #Con logia