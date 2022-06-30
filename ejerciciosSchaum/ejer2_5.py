import numpy as np
import csv

def csv_to_string(file):
    """
    Funcion para leer archivos csv
    """
    items = []
    try:
        with open(file, 'r') as archivo:
            render = csv.DictReader(archivo) # Transforma el archivo en un diccionario
            for line in render:
                items.append(line) #Agreda cada diccionario a la lista
        return items 
    except:
        return 'error de conexion'

cantidad_tiempo = csv_to_string('tabla2_5.csv')
porcentaje_menor_15 = 0
porcentaje_mayor_10 = 0
for dic in cantidad_tiempo:
    for key, data in dic.items():
        if(key=='Horas' and int(data) ==15):
            porcentaje_menor_15 = int(dic['Porcentajes_acumulados'])

        if(key=='Horas' and int(data) <=10):
            porcentaje_mayor_10 = porcentaje_mayor_10 + int(dic['Porcetajes_validos'])


print(f'El porcentaje acumulado correspondiente a 15 horas es: {porcentaje_menor_15}%')
print(f'''El porcentaje acumulado correspondiente a 10 horas es: {porcentaje_mayor_10}%
Es decir, {porcentaje_mayor_10}% usa su celular 10 horas o menos por semana.''')
