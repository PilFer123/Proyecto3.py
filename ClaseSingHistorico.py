# Funcion que define una clase para el uso del método singleton
# crea un archivo histórico y no permite la creacion de más archivos de la misma clase
class Singleton:            # clase singleton que solo permite el uso de un arhivo histórico
                            # para registrar los servicios prestados
    _instance = None

    def __init__(self):     # Llamado al metodo Init
        self.nombre = "Historial.txt"

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)   # invoca metodo nueva instancia
        return cls._instance

    def getNombre(self):        # Muestra el atributo nombre indicado x usuario
        print(self.nombre)

    def setValor(self, valor):
        self.nombre = valor

class UnicoArchivo:
    _instance = None
    file = None

    def __init__(self, nombreArchivo):
        self.matrix = [[1,2],[3,4],[5,6]]
        if self.file is None:
            self.file = open(nombreArchivo, 'w')

    def __new__(cls, *args, **kwargs):

        if not isinstance(cls._instance, cls):
            print("Creando el unico archivo")
            cls._instance = object.__new__(cls)

        return cls._instance

    def agregarLinea(self, linea):  # Escribe en el archivo
        self.file.write(linea + '\n')

