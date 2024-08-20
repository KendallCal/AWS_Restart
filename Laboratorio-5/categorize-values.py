print("============================= Categorización en Python =============================\n")

#Categorización de valores.
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

#Recorre la lista e imprime cada elemento.
for item in myMixedTypeList:
    print("{} es de tipo {}".format(item,type(item)))