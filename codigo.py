import pandas as pd
import zipfile
import os
import csv

archivo_zip = "data.zip"
def extraer_archivo(archivo_zip):
# Ruta al archivo ZIP


    # Ruta donde quieres extraer los archivos
#directorio_destino = "directorios"

    # Extraer el archivo ZIP
    with zipfile.ZipFile(archivo_zip, 'r') as zip_ref:
            zip_ref.extractall()

def leer_archivos(carpeta, n_carpeta):
    
    datos = []
    df = pd.DataFrame(datos, columns=["phrase", "sentiment"])
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".txt"):
            ruta_archivo = os.path.join(carpeta, archivo)
            with open(ruta_archivo, "r") as f:
                contenido = f.read()
                datos.append((contenido, n_carpeta))
                #df = df.append({"phrase":contenido,"sentimen": n_carpeta}, ignore_index=True)
                df.loc[len(df)] = {"phrase":contenido,"sentiment": n_carpeta}
    return df

archivos=["negative", "neutral", "positive"]
df2 = pd.DataFrame([], columns=["phrase", "sentiment"])
for carpeta in archivos:
    carpeta_a_recorrer = os.path.join('test', carpeta)
# Leer archivos de la carpeta y obtener datos
    datos = leer_archivos(carpeta_a_recorrer, carpeta)
    df2 = pd.concat([df2, leer_archivos(carpeta_a_recorrer, carpeta)], ignore_index=True)
# Crear DataFrame


# Mostrar DataFrame
#print(df.value_counts("sentimen"))
#print(df2.value_counts("sentimen"))
df2.to_csv("test_dataset.csv", index=False)