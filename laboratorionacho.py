class Producto():
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio

    def dame_nombre(self):
        return self.nombre

    def dame_precio(self):
        return self.precio

class Medicamento(Producto):
    def __init__(self,nombre,precio,compuestos,porcentaje):
        super().__init__(nombre,precio)
        self.compuestos=compuestos
        self.porcentaje=porcentaje

    def dame_compuestos(self):
        return self.compuestos

    def dame_porcentaje(self):
        return self.porcentaje

class Laboratorio():
    def __init__(self,nombre,lista_productos):
        self.nombre=nombre
        self.lista_productos=lista_productos

    def dame_info(self):
        return self.lista_productos

lista_productos1=[]
producto1=Producto("Champú anticaída",9)
producto2=Medicamento("Frenadol",4.5,"Ibuprofeno",76)
producto3=Medicamento("Dalsy",3,"Ibuprofeno",45)
lista_productos1.append(producto1.dame_nombre())
lista_productos1.append(producto2.dame_nombre())
lista_productos1.append(producto3.dame_nombre())
Laboratorio1=Laboratorio("Farmacianacho",lista_productos1)
print(Laboratorio1.dame_info())
