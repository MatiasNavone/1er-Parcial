def listainver(lista):
    if len (lista) == 0:
        return[]
    else:
        return listainver(lista[1:]) + [lista[0]]


lista = ["1","2","3","4","5"]
print(listainver(lista))
    