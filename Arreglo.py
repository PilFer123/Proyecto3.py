

class Publicacion:
    def __int__(self):
        self.autor = " "
        self.titulo = " "
        self.anno = " "
        self.editorial = " "

    def setDatos(self):
        self.autor = input("Autor: ")
        self.titulo = input("Título: ")
        self.editorial = input("Editorial: ")

class Libro (Publicacion):
    pass

class Revista (Publicacion):
    def __int__(self):
        super().__int__()
        self.volumen = " "
        self.anno = " "

    def setDatos(self):
        super().setDatos()
        self.volumen = input("Volumen: ")
        self.anno = input("Año de publiicación: ")

r = Revista()
arrObjs = []         # vector de objetos

for i in range(3):
    x = str("obj")+str(i)
    x = Revista()
    x.setDatos()
    arrObjs.append(x)
    print(f"Indice {i} dato {arrObjs[i].autor}")

for j in range(3):
    print("Indice: ",j)
    print(arrObjs[j].autor," ", arrObjs[j].titulo )

