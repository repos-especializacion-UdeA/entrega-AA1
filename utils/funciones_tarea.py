import os

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

