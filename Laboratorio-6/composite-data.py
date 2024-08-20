print("============================= Datos Compuestos en Python =============================\n")

#Librerias.
import csv
import copy

#Diccionario que funcionará como tipo de compuesto.
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

#Recorre las claves y valores del diccionario.
print("- - - - - - - - - - - Diccionario - - - - - - - - - - -")
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))

#Lista vacía para almacenar el inventario de los vehículos.
myInventoryList = []

#Lee el archivo CSV.
print("\n")

print("- - - - - - - - - - - Lee el archivo CSV y lo guarda en la lista vacía - - - - - - - - - - -")

with open('Laboratorio-6/car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')

#Recorre las claves y valores del diccionario.
print("\n")

print("- - - - - - - - - - - Recorre las claves y valores del diccionario - - - - - - - - - - -")

for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
        print("-----")

