print("============================= Controladores de Archivos y Módulos en Python =============================\n")

#Importa el módulo para manejar archivos JSON.
import jsonFileHandler  

#Lee el archivo JSON llamado y lo almacena.
data = jsonFileHandler.readJsonFile('Laboratorio-14/insulin.json')

#Verifica si los datos leídos no están vacíos.
if data != "":
    #Extrae las secuencias de insulina b y a desde los datos JSON.
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    
    #Concatena las secuencias de insulina b y a para obtener la secuencia completa de insulina
    insulin = bInsulin + aInsulin
    
    #Extrae el peso molecular actual de la insulina desde los datos JSON.
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    
    #Imprime la secuencia de insulina b.
    print('bInsulin: ' + bInsulin)
    
    #Imprime la secuencia de insulina a.
    print('aInsulin: ' + aInsulin)
    
    #Imprime el peso molecular actual de la insulina.
    print('\nPeso molecular actual de la insulina: ' + str(molecularWeightInsulinActual))
    
    #Calcula el peso molecular de la insulina. 
    #Obtiene una lista con los pesos de los aminoácidos desde los datos JSON.
    aaWeights = data['weights']
    
    #Cuenta el número de cada aminoácido en la secuencia de insulina.
    aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']})
    
    #Multiplica el conteo de cada aminoácido por su peso correspondiente.
    molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
    ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())
    
    #Imprime el peso molecular calculado de la insulina.
    print("\nEl peso molecular aproximado de la insulina: " +
    str(molecularWeightInsulin))
    
    #Imprime el porcentaje de error comparado con el peso molecular actual.
    print("\nPorcentaje de error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))
else:
    #Imprime un mensaje de error si los datos no se pudieron leer y termina el programa.
    print("\nError. Saliendo del programa...")