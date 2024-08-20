#Importa el módulo json para manejar archivos JSON.
import json

#Función para leer el archivo JSON.
def readJsonFile(fileName):
    data = ""
    try:
        #Intenta abrir el archivo JSON.
        with open(fileName) as json_file:
            #Guarda los datos.
            data = json.load(json_file)
            
    except IOError:
        #Si ocurre un error al intentar abrir o leer el archivo, muestra un mensaje de error.
        print("No se pudo leer el archivo.")
        
    return data  #Retorna el contenido del archivo JSON o una cadena vacía si hubo un error.
