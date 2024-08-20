print("============================= String en Python =============================\n")

#Valor de tipo String.
print(" - - - - - - - Tipo String (string) - - - - - - - ")

myString = "Esto es un String."

print(myString)

print(type(myString))

print(myString + " es un valor de tipo String " + str(type(myString)) + "\n\n")

#Concatenación de Strings.

print(" - - - - - - - Concatenación - - - - - - - ")

firstString = "Cafe"

secondString = " con "

thirdString = "leche."

concatenationString = firstString + secondString + thirdString

print("Concatenación de un string: " + concatenationString)

#Trabajar con inputs.
print("\n\n - - - - - - - Entradas (inputs) - - - - - - - ")

name = input("¿Cual es su nombre? ")

print("Nombre agregado: " + name)

color = input("\n¿Cual es tu color favorito? ")

animal = input("¿Cual es tu animal favorito? ")

print("\n{}, te gustan los {} {}!".format(name,animal,color))