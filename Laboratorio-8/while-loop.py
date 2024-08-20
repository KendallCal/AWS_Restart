print("============================= Bucle While - Loop (while) =============================\n")

#Bucle While.
import random

print("Bienvenido a Adivina el Número!")
print("Las reglas son simples. Yo pensaré en un número y tú intentarás adivinarlo.")

#Crea un número aleatorio entre 1-10.
number = random.randint(1,10)

#Variable para guardar si el usuario acepto.
isGuessRight = False

#Bucle ppara ver si lo adivino.
while isGuessRight != True:
    #Solicita el número al usuario.
    guess = input("Adivina el nombre entre 1 - 10: ")
    
    #Verifica si es correcto con una condicional.
    if int(guess) == number:
        print("\nSu elección: {}. Es correcto! Ganaste!".format(guess))
        isGuessRight = True
        
    else:
        print("Su elección: {}. Lo siento, no es correcto. Intenta de nuevo.".format(guess))