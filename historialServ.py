
class Singleton:
    _instance = None

    def __init__(self):     # Llamado al metodo Init
        self.nombre = "Historial"

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)   # invoca metodo nueva instancia
        return cls._instance

    def getNombre(self):        # Muestra el atributo nombre indicado x usuario
        print(self.nombre)

'''    
    def setValor(self, valor):
        self.nombre = valor
'''
class UnicoArchivo:
    _instance = None
    file = None

    def __init__(self, NombreArchivo):
        self.matrix = [[1,2],[3,4],[5,6]]
        if self.file is None:
            self.file = open(NombreArchivo, 'w')

    def __new__(cls, *args, **kwargs):

        if not isinstance(cls._instance, cls):
            print("Creando el unico archivo")
            cls._instance = object.__new__(cls)

        return cls._instance

    def agregarLinea(self, linea):
        self.file.write(linea + '\n')


# en el  principal:    from misClases inport Singleton

instancia1 = Singleton()

archivo = UnicoArchivo("Historial.txt")
archivo.agregarLinea("Hola mundo 1")

print("Utilizando el archivo: ", instancia1.getNombre())

instancia2 = Singleton()    #Podemos intentar crear otra instancia


print("Estamos utilizando el archivo; ", instancia2.getNombre())
instancia1.getNombre()


archivo2 = UnicoArchivo("Historico.txt")
archivo2.agregarLinea("No puede hacer otro archivo, ojo")
archivo2.agregarLinea("Linnea 3 ===> No puede hacer otro archivo")

