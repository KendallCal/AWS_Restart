print("============================= Funciones en Python =============================\n")

#Función para duplicar el alfabeto.
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

#Función para obtener un mensaje del usuario.
def getMessage():
    stringToEncrypt = input("\nPor favor ingrese un mensaje para cifrar: ")
    return stringToEncrypt

#Función para obtener una clave de cifrado del usuario.
def getCipherKey():
    shiftAmount = input("Por favor, introduzca una clave (número entero del 1 al 25): ")
    return shiftAmount

#Función para cifrar un mensaje usando la clave de cifrado y el alfabeto proporcionado.
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    
    #Convierte el mensaje a mayúsculas.
    uppercaseMessage = message.upper()  
    for currentCharacter in uppercaseMessage:
        #Encuentra la posición del carácter en el alfabeto.
        position = alphabet.find(currentCharacter)
        
        #Calcula la nueva posición después del desplazamiento.
        newPosition = position + int(cipherKey) 
        
        if currentCharacter in alphabet:
            #Construye el mensaje cifrado.
            encryptedMessage = encryptedMessage + alphabet[newPosition]  
        else:
            #Mantiene caracteres no alfabéticos sin cambios.
            encryptedMessage = encryptedMessage + currentCharacter  
    return encryptedMessage

#Función para descifrar un mensaje usando la clave de cifrado y el alfabeto proporcionado.
def decryptMessage(message, cipherKey, alphabet):
    #Convierte la clave de cifrado en clave de descifrado.
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

#Función principal para ejecutar el programa de cifrado César.
def runCaesarCipherProgram():
    #Define el alfabeto.
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  
    print(f'Alphabet: {myAlphabet}')
    
    #Obtiene el alfabeto duplicado.
    myAlphabet2 = getDoubleAlphabet(myAlphabet)  
    print(f'Alphabet2: {myAlphabet2}')
    
    #Obtiene el mensaje a cifrar.
    myMessage = getMessage()
    print(myMessage)
    
    #Obtiene la clave de cifrado.
    myCipherKey = getCipherKey()  
    print(myCipherKey)
    
    #Cifra el mensaje.
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)  
    print(f'\nMensaje cifrado: {myEncryptedMessage}')
    
    #Descifra el mensaje.
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Mensaje descifrado: {myDecryptedMessage}')

#Ejecuta el programa de cifrado César.
runCaesarCipherProgram()
