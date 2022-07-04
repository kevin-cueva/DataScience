import numpy as np

#Puntuacines
matriz = np.array([[88,45,53,86,33,86,85,30,89,53,41,96,56,38,62],
                   [71,51,86,68,29,28,47,33,37,25,36,33,94,73,46],
                   [42,34,79,72,88,99,82,62,57,42,28,55,67,62,60],
                   [96,61,57,75,93,34,75,53,32,28,73,51,69,91,35]])

array = np.sort(matriz.flatten()) # Organizados de menor a mayor

print(f'Q1: {np.percentile(array,25)} - el 25% saco menos de {np.percentile(array,25)}')
print(f'Q2: {np.percentile(array,50)} ')
print(f'Q3: {np.percentile(array,75)} ')
print(f'D9: {np.percentile(array,90)} ')
print(f'P95: {np.percentile(array,95)} ')