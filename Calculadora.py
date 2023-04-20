

class Prueba:
    def __int__(self):
        self.nombre = "Marta"
        self.edad = "22"
        self.telef = "5355365"


obj1 = Prueba()

import numpy as np

mat1 = np.array ([obj1, obj1, obj1, obj1])
obj1.nombre = "Marta"
obj1.edad = "24"
obj1.telef = "345334"


arr_obj2 = [obj1,obj1,obj1,obj1]


for i in range(3):
    arr_obj2.append(obj1)
    arr_obj2[i].nombre = input("Nombre: ")
    arr_obj2[i].edad = input("Edad: ")
    print(i)

print()
for i in range(3):
    print(arr_obj2[i].nombre)

