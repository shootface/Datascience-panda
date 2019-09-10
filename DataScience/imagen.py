import pandas as pd
import numpy as np
import matplotlib as mpl
#mpl.use('Agg')
import matplotlib.pyplot as plt
#libreria de scipy que contiene funciones varias
#scikit-image es una colección de algoritmos de procesamiento de imágenes para Python. 
#Realiza tareas como la carga de imágenes, el filtrado, la morfología, la segmentación, 
#las conversiones de color y las transformaciones.
from scipy import misc
from scipy import stats
#Imagen de Ejemplo escalera   
escalera=misc.ascent()
#shape retorna las dimensiones del arreglo
print(escalera)
print(escalera.shape)
plt.imsave('escaleraOriginal.png', escalera)
xmax=escalera.shape[0]
ymax=escalera.shape[1]
print(xmax)
print(ymax)
escalera[range(xmax),range(ymax)]=0# los pixeles de la diagonal principal se igualan a 0 es decir se "pintan de negro"
print(type(escalera))
plt.imsave('escaleraDiagonalNegra.png', escalera)#imsave guarda la imagen en un nuevo archivo
escalera[range(xmax-1,-1,-1),range(ymax)]=0
plt.imsave('escaleraXNegra.png', escalera)

cmap = plt.cm.gray#cm representa el mapa de color Consultar mapas de color disponibles
plt.imsave('escaleraGray.png', escalera,cmap=cmap)
cmap = plt.cm.Spectral 
plt.imsave('escaleraPrueba.png', escalera,cmap=cmap)
acopy=escalera.copy()
plt.imsave('escaleraCopy.png', acopy)
plt.imsave('test2.png', escalera,cmap=cmap)
def get_indices(size):
   arr = np.arange(size)
   return arr % 4 == 0

cmap = plt.cm.gray
escalera1 = escalera.copy() 
xindices = get_indices(escalera.shape[0])
yindices = get_indices(escalera.shape[1])
escalera1[xindices, yindices] = 0
plt.imsave('escalera.png', escalera1,cmap=cmap)
escalera2 = escalera.copy() 

# Between quarter and 3 quarters of the max value
escalera2[(escalera < escalera.max()/2)]=0# los pixeles que tengan un valor inferior a la mitad del maximo seran convertidos a negro

plt.imsave('escalera2.png', escalera2,cmap=cmap)
