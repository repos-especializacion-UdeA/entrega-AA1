import os
import matplotlib.pylab as plt
import scipy.io
from scipy import signal
import pandas as pd
import numpy as np

# Promt to @Chat-GPT: obtener la lista de archivos .mat de un directorio en python
def obtener_archivos_mat(directorio):
    """Obtiene una lista de todos los archivos .mat en un directorio dado."""
    archivos_mat = [archivo for archivo in os.listdir(directorio) if archivo.endswith('.mat')]
    return archivos_mat

# Promt to @Chat-GPT: crear tabla Markdown a partir de una lista 
def crear_tabla_markdown(lista_de_datos):    
    """Convierte una lista de listas en una tabla Markdown.
    
    Ejemplos 
    datos = [
              ["Nombre", "Edad", "Ciudad"],
              ["Ana", "23", "Madrid"],
              ["Luis", "35", "Barcelona"],
              ["Marta", "29", "Valencia"]
            ]
    tabla_markdown = crear_tabla_markdown(datos)
    """
    # Encabezados de la tabla
    encabezados = lista_de_datos[0]
    filas = lista_de_datos[1:]

    # Crear la tabla
    tabla_markdown = '| ' + ' | '.join(encabezados) + ' |\n'
    tabla_markdown += '| ' + ' | '.join(['---'] * len(encabezados)) + ' |\n'

    # Añadir filas
    for fila in filas:
        tabla_markdown += '| ' + ' | '.join(fila) + ' |\n'

    return tabla_markdown


# Promt to @Chat-GPT: crear lista no numerada en markdown a partir de una lista en python
def crear_lista_markdown(lista):
    """Convierte una lista de Python en una lista no numerada en formato Markdown."""
    lista_markdown = ""
    for elemento in lista:
        lista_markdown += f"- {elemento}\n"
    return lista_markdown

####################################################################################################
# Funciones sobre las señales
####################################################################################################


# Numero del estimulo
def indice_numero(df, num):
  return (df.index[df == num][0],df.index[df == num][-1])

# Cambios de nivel
def detectar_cambios_nivel(data, valor):
    cambios = []
    for i in range(1, len(data)):
        if data[i] == valor and data[i-1] != valor:
            cambios.append((i-1,0))
            cambios.append((i,valor))
        elif data[i] != valor and data[i-1] == valor:
            cambios.append((i-1,valor))
            cambios.append((i,0))
    cambios.pop(0)
    cambios.pop()
    return cambios


####################################################################################################
# Funciones de graficado
####################################################################################################

def graficar_medida(medida, 
                    fs = None,
                    columnas = None, 
                    titulo = None, 
                    etiqueta_x = None, 
                    etiqueta_y = None):
    plt.figure(figsize=(20, 4))  # Tamaño del gráfico
    
    # Iterar sobre cada columna en la lista de columnas
    if fs is None:
        t = medida.index
    else:
        t = 1/fs*medida.index

    if not isinstance(medida, pd.DataFrame):
        t = np.arange(0,len(medida))
        if fs is not None:
            t = 1/fs*t
        plt.plot(t,medida)  # Graficar cada columna
    else:
        if (columnas is None):
            columnas = medida.columns      
        for columna in columnas:
            plt.plot(t, medida[columna], label=columna)  # Graficar cada columna

    # Añadir títulos y etiquetas
    if etiqueta_x is None: 
        etiqueta_x = "muestras [n]"
        if fs is not None:
            etiqueta_x = "tiempo [s]"

    if etiqueta_y is None: 
        etiqueta_y = "Amplitud"
    
    plt.title(titulo)
    plt.xlabel(etiqueta_x)
    plt.ylabel(etiqueta_y)
    plt.legend()  # Añadir la leyenda para distinguir las columnas
    plt.grid(True)  # Añadir cuadrícula
    plt.show()

    """
    graficar_varias_columnas(emgs,
                         columnas = emgs.columns,
                         titulo = "Grafico canales EMG",
                         etiqueta_x="n",
                         etiqueta_y="Amplitud")
    """

if __name__ == "__main__":
    muestra_mat = scipy.io.loadmat("./S1_A1_E1.mat")
    df_emg = pd.DataFrame(muestra_mat['emg'])
    print(df_emg.shape)
    df_restimulus = pd.DataFrame(muestra_mat['restimulus'])
    print(df_restimulus.shape)
    df_repetition = pd.DataFrame(muestra_mat['rerepetition'])
    print(df_repetition.shape)
    keys_mat_data = list(muestra_mat.keys())
    column_names = keys_mat_data[3:]
    # graficar_medida(df_emg)
    # graficar_medida(df_emg, fs = 100)
    # graficar_medida(df_emg, columnas = [0])    
    # graficar_medida(df_emg, fs = 100, columnas = [0])    
    # graficar_medida(df_emg[0])    
    graficar_medida(df_emg[0], fs = 100)    