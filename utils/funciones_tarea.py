import os
import glob


# Promt to @Chat-GPT: crear lista no numerada en markdown a partir de una lista en python
def hola():
    """Convierte una lista de Python en una lista no numerada en formato Markdown."""
    print("hola")

# Promt to @Chat-GPT: obtener la lista de archivos .mat de un directorio en python
def obtener_archivos_mat(directorio):
    """Obtiene una lista de todos los archivos .mat en un directorio dado."""
    patron = os.path.join(directorio, "*.mat")
    archivos_mat = glob.glob(patron)
    return archivos_mat


