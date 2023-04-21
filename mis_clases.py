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

###########################################################3
# definición clase Usuarios
class Usuario():                #  clase Usuarios

    def __int__ (self):
        self.identif = " "
        self.nombre = " "
        self.telefono = " "


    def mostrarUsuario(self):       # retorna los datos del usuario
        return "Num. Identif: {} Nombre: {}, tel. {}".format(self.identif, self.nombre,self.telefono)

    def nuevoUsuario(s):            # lee datos de un NUEVO usuario
        s.cedula = input("Num. Identificación: ")
        s.nombre = input("Nombre de Usuario: ")
        s.telefono = input("Telefono de Usuario: ")
        return s

###########################################################
# definición clase Servicios (Prestamo/Devolución)
class Servicio():    # definición clase Servicio
    def __int__(self):
        self.idServicio = " "
        self.descripc = ""
        self.fechInic = ""
        self.fechfinal = ""
        self.idUsu = ""
        self.nombreUsu = ""
        self.telefUsu = ""

    def mostrarServicio(self):      # Retorna datos de servicio
        return "Identif de Servicio: {}, Tipo de servicio:{}, Fecha Inicio: {}, " \
               "Fecha devolución: {}, Identif. del Usuario: {}, " \
               "Nombre del Usuario: {}, elefono del Usuario: {}" \
               " ".format(self.idServicio, self.descripc, self.fechInic, self.fechfinal,
                          self.idUsu, self.nombreUsu, self.telefUsu)

    def getServicio(s):        # registrar nuevo servicio
        s.idServicio = input("Identif de Servicio ")
        s.descripc = input("Tipo de servicio (préstamo, devolución, pérdida, otro): ")
        s.fechInic = input("Fecha Inicio: ")
        s.fechfinal = input("Fecha devolución: ")
        s.idUsu = input("Identif. del Usuario: ")
        s.nombreUsu = input("Nombre del Usuario: ")
        s.telefUsu = input("Telefono del Usuario")
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
