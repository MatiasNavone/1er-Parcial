class Pila:
    def _init_(self):
        self.items = []
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None
    
    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return None
    
    def tamano(self):
        return len(self.items)
    
from dino import dinosaurios

#a cuantas especies hay
def contar_especies(dinosaurios):
    especies = set()
    for dino in dinosaurios:
        especies.add(dino["especie"])
    return len(especies)


#b cuantos descubridores hay
def contar_descubridores(dinosaurios):
    descubridores = set()
    for dino in dinosaurios:
        descubridores.add(dino["descubridor"])
    return len(descubridores)


#c dinosaurios que empiecen con T
def mostrar_dinosaurios_con_t(dinosaurios):
    for dino in dinosaurios:
        if dino["nombre"].startswith("T"):
            print(dino["nombre"])


#d dinosaurios que pesen menos de 275 Kg
def mostrar_dinosaurios_ligeros(dinosaurios):
    for dino in dinosaurios:
        peso_str = dino["peso"].split()[0]  
        peso = int(peso_str) if peso_str.isdigit() else None  
        if peso is not None and peso < 275:
            print(dino["nombre"])


#e lista aparte de todos los dinosaurios que comienzan con A, Q, S
def separar_dinosaurios(dinosaurios):
    dinosaurios_separados = []
    for dino in dinosaurios:
        if dino["nombre"][0].upper() in ['A', 'Q', 'S']:
            dinosaurios_separados.append(dino)
    return dinosaurios_separados



print("Cantidad de especies:", contar_especies(dinosaurios))
print("Cantidad de descubridores distintos:", contar_descubridores(dinosaurios))

print("Dinosaurios que empiezan con T:")
mostrar_dinosaurios_con_t(dinosaurios)

print("Dinosaurios que pesan menos de 275 Kg:")
mostrar_dinosaurios_ligeros(dinosaurios)

print("Dinosaurios que comienzan con A, Q, S:")
dinosaurios_separados = separar_dinosaurios(dinosaurios)
for dino in dinosaurios_separados:
    print(dino["nombre"])