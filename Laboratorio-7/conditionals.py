print("============================= Condicionales en Python (if-else-elif) =============================\n")

#Condicionales en Python.
userReply = input("¿Necesita enviar un paquete? (Ingrese si o no) ")

#Condicional IF - ELSE.
if userReply == "Si" or userReply == "si" or userReply == "Sí" or userReply == "sí":
    print("Podemos ayudar a enviar el paquete!")
else:
    print("Por favor, vuelva cuando necesite enviar un paquete. Gracias.")

#Ejemplo de elif.
userReply = input("\n\n¿Quieres comprar sellos, comprar un sobre o hacer una copia? (Elija: Sellos, Sobre, Copia) ")

if userReply == "Sellos" or userReply == "sellos":
    print("Tenemos muchos diseños de sellos para elegir.")
    
elif userReply == "Sobre" or userReply == "sobre":
    print("Disponemos de muchos tamaños de sobres para elegir.")
    
elif userReply == "Copia" or userReply == "copia":
    copies = input("¿Cuántas copias desea? (Introduzca un número) ")
    print("Aqui hay {} copias.".format(copies))
    
else:
    print("Muchas gracias. Por favor, vuelve otra vez.")