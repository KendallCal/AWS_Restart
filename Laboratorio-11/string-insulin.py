print("============================= String Insulina con Python =============================\n")

#Almacena la secuencia de preproinsulina humana.
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

#Almacenar los elementos de las secuencias.
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

#Concatena los datos a y b.
insulin = bInsulin + aInsulin

#Imprime la asecuencia de preproinsulina.
print("La secuencia de la preproinsulina humana: ")

print(preproInsulin)

#Imprime la secuencia a.
print("\nLa secuencia de la insulina humana, cadena a: " + aInsulin)

#Calcula el peso molecular de la insulina.
#Crear una lista de los pesos de los aminoácidos (AA).
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}  

#Cuena la cantidad de cada aminoácido.
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})

#Multiplica la cantidad por los pesos.
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())  

#Imprime el peso molecular aproximado.
print("\nEl peso molecular aproximado de la insulina: " + str(molecularWeightInsulin))

#Guarda el Peso molecular real de la insulina.
molecularWeightInsulinActual = 5807.63

#Imprime el porcentaje de error.
print("\nPorcentaje de error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))
