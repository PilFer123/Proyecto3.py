# Proyecto 1: Curso de Programación
# Elaborado por M. Pilar Fernández Rodríguez
# I Cuatrimestre 2023

import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

from mis_clases import Libro, Revista, Servicio
from Calculadora import Calc
from ClaseSingHistorico import Singleton, UnicoArchivo
def LimpiarPant():
    for a in range(30):
        print(" ")

def MostrarPublic():        # Muestra las Publicaciones almacenadas
    print("            Mostrar Publicaciones        ")
    print("Libros Registrados ")
    for j in range(len(arrLib)):
        print(f"Autor: {arrLib[j].autor} Título: {arrLib[j].titulo} "
              f"Editorial: {arrLib[j].editorial} Año: {arrLib[j].anno} ")
    print()
    print("Revistas Registradas ")
    for i in range(len(arrRev)):
        print(f"Autor: {arrRev[i].autor} Título: {arrRev[i].titulo} "
              f"Editorial: {arrRev[i].editorial} Año: {arrRev[i].anno} "
              f"Vol.: {arrRev[i].volumen} Número: {arrRev[i].numero}")
    print()

def NuevoLibro():       # Registra nuevos libros
    print("            Registrar NUEVOS Libros               ")
    z = 0
    while z >= 0:
        try:
            z = int(input("Cúantos libros desea registrar: "))
            break
        except:
            print("Error: Debe digitar un numero entero")
            continue

    for i in range(z):
        print("Ingresando libro ", i + 1)
        x = str("obj") + str(i)
        x = Libro()  # Instanciar Libros clase heredada de clase Publicaciones
        x.setDatos()
        arrLib.append(x)
        print()

def NuevoRevista():         # Registra nuevas revistas
    print("            Registrar NUEVAS Revistas             ")
    ctrl = 0
    while ctrl >= 0:
        try:
            ctrl = int(input("Cúantas Revistas desea registrar: "))
            break
        except:
            print("Error: Debe digitar un numero entero")
            ctrl = 0
            continue

    for i in range(ctrl):
        print("Ingresando Revista ", i + 1)
        y = str("obj") + str(i)
        y = Revista()  # Instanciar Revista clase heredada de clase Publicaciones
        y.setDatos()
        arrRev.append(y)
    print()

def NuevoServicio():    # Registra nuevos servicios
    i = 0                   # Almacena la información en el fichero
    ctrl = True
    #fichero = open("Historial.txt", 'a')
    while ctrl == True:
        print()
        print("Ingresando datos de Nuevo Servicio ")
        print()
        i = i + 1
        k = str("obj") + str(i)
        k = Servicio()
        k.SetServicio()
        arrServ.append(k)

        lista = k.idServicio+" "+k.descripc+" "+k.fechInic+" "+k.fechfinal+" "+\
            k.idUsu+" "+k.nombreUsu+" "+k.telefUsu
        # Abrimos el fichero
        fichero = open("Historial.txt", 'a')

        # Guardamos la lista en el fichero
        fichero.writelines(lista + "\n")

        # Cerramos el fichero
        fichero.close()

        # almacenar costos de servicios
        print("\n Registro de costos por el servicio prestado")
        while True:
            try:
                dicCostos[k.idServicio]= float(input("==> Digite el costo del servicio?: "))
                break
            except:
                print("  ==> Error en el valor digitado \n")
                continue
        print()
        if (input("\n Necesita registrar más servicios (S/N): ") in ["S","s"]): ctrl = True
        else: ctrl = False
    print()
def MostrarServicio():
    print(arrServ)   # ver el contenido del arreglo
    for j in range(len(arrServ)):
        k = arrServ[j]
        print("Id. Servicio:    ", k.idServicio)
        print("Descripción:     ", k.descripc)
        print("Fecha Inic:      ", k.fechInic)
        print("Fecha Fin.       ", k.fechfinal)
        print("Id. Usuario:     ", k.idUsu)
        print("Nombre Usuario:  ", k.nombreUsu)
        print("Telef. Usuario:  ", k.telefUsu)
        print()

def IngPorServ():
    tot = 0
    # Imprime los valores del diccionario
    for x in dicCostos:
        print(dicCostos[x])
        tot = tot + dicCostos[x]
    print(f"El total de ingresos es: {tot}")

def MostrarArchivo():       # presenta los datos del fichero
    print("Id.Servicio Desc. F.Inic. F.Fin IdUsu. NomUsu TelUsu")
    with open('Historial.txt', 'r') as archivo:
        linea = archivo.readline()
        while linea != '':
            print(linea, end='')
            linea = archivo.readline()
    archivo.close()


# MAIN
if __name__ == "__main__":
    #k = Servicio()
    inst = Singleton()
    archivo = UnicoArchivo("Historial.txt")

    arrLib = []
    arrRev = []
    arrServ = []
    dicCostos = {}
    opcTupla = ("1","2","3","4","5","6","7","8","0")

    opc = 1
    while opc != 0:             # mostrar MENU PRINCIPAL
        LimpiarPant()
        clear()
        print("+++++++++++++++++++++++++++++++++++++++++++")
        print("¨¨¨UNIVERSIDAD ESTATAL A DISTANCIA¨¨¨¨¨¨¨¨¨")
        print("¨¨¨Carrera de Informática Educativa¨¨¨¨¨¨¨¨")
        print("¨¨¨¨¨¨¨¨Curso: Programación III¨¨¨¨¨¨¨¨¨¨¨¨")
        print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨Proyecto #2 ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
        print("                                           ")
        print("             MENU PRINCIPAL                ")
        print("                                           ")
        print("    OPC 1: Registrar Nuevos Libros         ")
        print("    OPC 2: Registrar Nuevas Revistas       ")
        print("                                           ")
        print("    OPC 3: Mostrar Publicaciones           ")
        print("                                           ")
        print("    OPC 4: Registrar Servicio              ")
        print("    OPC 5: Mostrar Servicios Registrados   ")
        print("    OPC 6: Mostrar Fichero                 ")
        print("                                           ")
        print("    OPC 7: CALCULAR DEUDAS X Servicios     ")
        print("    OPC 8: Cobro por Servicios             ")
        print("                                           ")
        print("    OPC 0: Finalizar                       ")
        print("+++++++++++++++++++++++++++++++++++++++++++")
        opc = input("Digite una opción: 1,2,3,4,5,6,7,8 o 0 para finalizar: ")
        LimpiarPant()
        clear()
        if not(opc in opcTupla):    # error: no digitó un número
            control = input("Error al digitar la opción, Presione ENTER para continuar ==>")
            continue
        elif opc == "1":
            print("         Opc 1:  Registrar nuevos libros ")
            NuevoLibro()

        elif opc == "2":
            print("         Opc 2:  Registrar nuevas Revistas ")
            NuevoRevista()

        elif opc == "3":
            print("         Opc 3:  Mostrar Publicaciones registradas")
            MostrarPublic()

        elif opc == "4":
            print("         Opc 4: Registrar Nuevo servicio    ")
            NuevoServicio()
            print()

        elif opc == "5":
            print("         Opc 5: Mostrar servicios registrados   ")
            MostrarServicio()
            print()

        elif opc == "6":
            print("         Opc 6: Mostrar Información del Fichero  ")
            print()
            MostrarArchivo()
            print()

        elif opc == "7":            # OPC 7: CALCULAR DEUDAS por Servicios
            print("            C A L C U L A D O R A            ")
            Calc()

        elif opc == "8":
            # Mostrar ingresos por prestación de servicios
            # datos almacenados en diccionario dicCostos
            IngPorServ()

        else:
            # finalizar el ciclo
            break
        control = input("\n Presione ENTER para continuar ==> ")
    print(" Fin del ciclo ")




