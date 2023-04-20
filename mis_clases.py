# Definición de clases
###########################################################


class Publicacion:          # definición clase Publicación
    def __int__(self):
        self.autor = " "
        self.titulo = " "
        self.anno = " "
        self.editorial = " "

    def setDatos(self):
        self.autor = input("Autor: ")
        self.titulo = input("Título: ")
        self.anno = input("Año: ")
        self.editorial = input("Editorial: ")

class Libro (Publicacion):
    pass

class Revista (Publicacion):
    def __int__(self):
        super().__int__()
        self.volumen = " "
        self.edicion = " "

    def setDatos(self):
        super().setDatos()
        self.volumen = input("Volumen: ")
        self.edicion = input("Edición: ")

'''
class Libro():
    #  clase Libros
    def __int__(self):
        self.autor = ""
        self.titulo = ""
        self.anno = 0
        self.estado = ""      # posibles estados: disponible, prestado, perdido, otro

    def mostrarLibro(self):
        # Retorna los datos de cada libro
        return "Au: {}, Tit. {}, año. {}, estado {}".format(self.autor, self.titulo, self.anno, self.estado)

    def nuevoLibro(s):
        # lee por teclado la información de un NUEVO libro
        s.autor = input("Autor: ")
        s.titulo = input("Título: ")
        s.anno = input("Año: ")
        s.estado = input("Estado: ")
        return s
'''
###########################################################3
# definición clase Usuarios
class Usuario():
    #  clase Usuarios
    def __int__ (self):
        self.cedula = ""
        self.nombre = ""
        self.telefono = ""
        self.categoria = ""

    def mostrarUsuario(self):
        # retorna los datos de cada usuario
        return "Nombre: {}, tel. {}, Recor. {}".format(self.nombre,self.telefono,self.categoria)

    def nuevoUsuario(s):
        # lee por teclado los datos de un NUEVO usuario
        s.cedula = input("Cedula: ")
        s.nombre = input("Nombre: ")
        s.telefono = input("Telefono: ")
        s.categoria = input("Categoria: ")
        return s


###########################################################
# definición clase Servicio (Prestamo/Devolución)
class Servicio():
    # definición clase Servicio
    def __int__(self):
        self.cedula_usu = ""
        self.tipo_serv = ""
        self.nom_lib = ""
        self.fech_serv = ""
        self.fech_vec = ""

    def mostrarServicio(self):
        # Retorna datos de servicio solicitado
        return "Usuario: {}, Ser.{}, libro {}, f.prest. {}, f.vec. {} ".format(self.cedula_usu,self.tipo_serv,self.nom_lib,self.fech_serv,self.fech_vec)

    def nuevoServicio(s):
        # Leer por tecladdo nuevos servicios
        s.cedula_usu = input("Cedula Usuario: ")
        s.tipo_serv = input("Tipo de servicio: ")
        s.nom_lib = input("Nombre del Libro: ")
        s.fech_serv = input("fecha de préstamo: ")
        s.fech_vec = input("fecha de vecimiento: ")
        return s



###########################################################
# definición Clase Calculadora de precios
class Calc:
    def __init__(self, n1, n2):
        self.sumar = n1 + n2
        self.restar = n1 - n2
        self.multr = n1 * n2
        self.dividr = n1 / n2
        return
