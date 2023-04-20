# Proyecto 1: Curso de Programación
# Elaborado por M. Pilar Fernández Rodríguez
# I Cuatrimestre 2023

import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


from mis_clases import *

'''

def datosServicios():
    #inicializar datos servicios
    servicio1.cedula_usu = "27373737"
    servicio1.tipo_serv = "Prestamo"
    servicio1.nom_lib = "Hola"
'''
def limpiar_pant():
    for a in range(30):
        print(" ")

# MAIN
if __name__ == "__main__":
    s = Servicio()
    u = Usuario()


    l = Libro()         # Instanciar Libros clase heredada de clase Publicaciones
    r = Revista()       # Instanciar Revista, clase heredada de clase Publicaciones
    arrObjs = []        # vector de objetos para almacenar libros y revistas
    arrRev = []

    opc = 1
    while opc != 0:
        limpiar_pant()
        clear()
        # mostrar MENU PRINCIPAL
        print("+++++++++++++++++++++++++++++++++++++++++++")
        print("¨¨¨UNIVERSIDAD ESTATAL A DISTANCIA¨¨¨¨¨¨¨¨¨")
        print("¨¨¨Carrera de Informática Educativa¨¨¨¨¨¨¨¨")
        print("¨¨¨¨¨¨¨¨Curso: Programación III¨¨¨¨¨¨¨¨¨¨¨¨")
        print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨Proyecto #1 ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
        print("                                           ")
        print("             MENU PRINCIPAL                ")
        print("                                           ")
        print("    OPC 1: Registrar Nuevos Libros         ")
        print("    OPC 2: Registrar Nuevas Revistas       ")
        print("                                           ")
        print("    OPC 3: Mostrar Publicaciones           ")
        print("                                           ")
        print("                                           ")
        print("    OPC 5: Mostrar servicio                ")
        print("    OPC 6: NUEVOS servicios                ")
        print("                                           ")
        print("    OPC 7: CALCULAR DEUDAS X servicios     ")
        print("    OPC 8: Cobro por Servicios     ")
        print("                                           ")
        print("    OPC 0: Finalizar                       ")
        print("+++++++++++++++++++++++++++++++++++++++++++")
        opc = input("Digite una opción: 1,2,3,4,5,6,7,8 o 0 para finalizar: ")
        limpiar_pant()
        if not(opc in ["1","2","3","4","5","6","7","8","0"]):
            # no digitó un número
            control = input("Error al digitar la opción, Presione ENTER para continuar ==>")
            continue
        elif opc == "1":                  # Opc 1 = Registrar nuevos libros
            print("            Registrar NUEVOS Libros               ")
            z = int(input("Cúantos libros desea registrar: "))
            for i in range(z):
                print("Ingresando libro ",i+1)
                x = str("obj") + str(i)
                x = Libro()
                x.setDatos()
                arrObjs.append(x)
            print()
        elif opc == "2":                  # Opc 2 = Registrar nuevas Revistas
            print("            Registrar NUEVAS Revistas             ")
            z = int(input("Cúantas Revistas desea registrar: "))
            for i in range(z):
                print("Ingresando Revista ", i+1)
                y = str("obj") + str(i)
                y = Revista()
                y.setDatos()
                arrRev.append(y)
            print()

        elif opc == "3":
            # Mostrar Publicaciones registradas
            print("            Mostrar Publicaciones        ")
            print("Libros Registrados")
            for j in range(len(arrObjs)):
                print(arrObjs[j].autor, " ", arrObjs[j].titulo)
            print()
            print("Revistas Registradas")
            for i in range(len(arrRev)):
                print(arrRev[i].autor, " ", arrRev[i].titulo)
            print()

        elif opc == "4":
            print("            Solicitar Préstamo               ")
            print()

        elif opc == "5":
            print("            Solicitar Devolución           ")
            print()

        elif opc == "6":
            # agrega nuevos Servicios
            print("            NUEVOS Servicios            ")
            print()
            s.nuevoServicio()
            print(s.mostrarServicio())
            print()
        elif opc == "7":
            # Calculadora de multas por morocidad
            valor1 = 0
            valor2 = 0
            # operaciones a realizar
            control = " "
            while (control != ("s" or "S")):
                print("         CALCULADORA DEL SISTEMA ")
                print()
                # leer la operación a realizarr
                oper = input("==> Digite la operación a realizar (+, -, *, /): ")
                if oper in ["+", "-", "*", "/"]:
                    print()
                    # leer los valores
                    valor1 = float(input("==> Digite el PRIMER valor ==> "))
                    valor2 = float(input("==> Digite el SEGUNDO valor ==> "))
                    print()
                    # calcular el resultado de la operación
                    result = Calc(valor1, valor2)
                    if oper == "+":
                        print("El resultado de la suma es: ", result.sumar)
                    elif oper == "-":
                        print("El resultado de la resta es: ", result.restar)
                    elif oper == "*":
                        print("El resultado de la multiplicación es: ", result.multr)
                    elif oper == "/":
                        print("El resultado de la división es: ", result.dividr)
                    else:
                        print()
                else:
                    print("===> Error en el operador indicado ")
                print()
                control = input("===> Digite 'S' o 's' para finalizar o ENTER para continuar: ")
                limpiar_pant()
                print()
        elif opc == "8":
            # Registrar ingresos por prestación de servicios
            result = 0
            matr1 = [0,1,2,3]
            for i in range(4):
                matr1[i] = float(input(f"Digite los ingresos #{i+1} $:"))
                result += matr1[i]
            print(matr1)
            print(f"Total de ingresos ${result}")
        else:
            # finalizar el ciclo
            break
        control = input("Presione ENTER para continuar ==> ")
    print(" Fin del ciclo ")
