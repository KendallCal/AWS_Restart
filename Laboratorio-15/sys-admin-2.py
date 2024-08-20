print("=============================== Administración de sistemas en Python (subprocess) ===============================")

#Importa el módulo subprocess para ejecutar comandos del sistema.
import subprocess

#Ejecuta el comando "ls -l" usando subprocess.run, que lista los archivos y directorios en el directorio actual en formato largo.
print("\n- - - - - - - - - - - - - - - - - - - - Lista los archivos y directorios (ls -l) - - - - - - - - - - - - - - - - - - - -")

subprocess.run(["ls", "-l"])

#Ejecuta el comando "ls -l README.md" usando subprocess.run, que lista detalles del archivo README.md en formato largo.
print("\n\n- - - - - - - - - - - - - - - - - - Lista detalles del archivo README (ls -l README.md) - - - - - - - - - - - - - - - - - -")

subprocess.run(["ls", "-l", "README.md"])

#Define el comando y su argumento para recopilar información del sistema.
command = "uname"
commandArgument = "-a"

#Imprime un mensaje indicando el comando que se va a ejecutar.
print("\n\n- - - - - - - - - - - - - - - - - - Imprime el comando que se va a ejecutar (uname -a) - - - - - - - - - - - - - - - - - -")

print(f'Recopilación de información del sistema con el comando: {command} {commandArgument}\n')

#Ejecuta el comando "uname -a" usando subprocess.run, que muestra información del sistema.
subprocess.run([command, commandArgument])

#Define el comando y su argumento para recopilar información de los procesos activos.
command = "ps"
commandArgument = "-x"

#Imprime un mensaje indicando el comando que se va a ejecutar.
print("\n\n- - - - - - - - - - - - - - - - - -  Imprime el comando que se va a ejecutar (ps -x) - - - - - - - - - - - - - - - - - -")

print(f'Recopilación de información del proceso activo con el comando: {command} {commandArgument}\n')

#Ejecuta el comando "ps -x" usando subprocess.run, que muestra información sobre los procesos activos.
subprocess.run([command, commandArgument])
