print("============================= Cálcula la carga neta de la insulina =============================\n")

#Almacena la secuencia de preproinsulina.
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  

#Almacena las secuencias de la insulina.
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin

#Diccionario con los valores de pKR para diferentes aminoácidos.
pKR = {
    'y': 10.07,
    'c': 8.18,
    'k': 10.53,
    'h': 6.00,
    'r': 12.48,
    'd': 3.65,
    'e': 4.25
}

#Cuenta la cantidad de 'Y' en la secuencia de insulina.
insulin.count("Y")

#Convierte el conteo de 'Y' a un número flotante.
float(insulin.count("Y"))

#Cuenta la cantidad de cada aminoácido en la secuencia de insulina.
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})

#Inicializa el pH.
pH = 0

#Calcula la carga neta en diferentes valores de pH y muestra los resultados.
while (pH <= 14):
    netCharge = (
        +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
        for x in ['k','h','r']}.values()))
        -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
        for x in ['y','c','d','e']}.values())))
    print('{0:.2f}'.format(pH), netCharge)
    pH += 1