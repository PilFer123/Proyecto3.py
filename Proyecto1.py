# Proyecto 1: Curso de Programación
# Elaborado por M. Pilar Fernández Rodríguez
# I Cuatrimestre 2023

import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


from mis_clases import *


# Almacenar datos de Libros
def datos_libros():

# Almacena datos de Usuarios
def datos_usuarios():
    # completar datos de usuarios


def datosServicios():
    #inicializar datos servicios
    servicio1.cedula_usu = "27373737"
    servicio1.tipo_serv = "Prestamo"
    servicio1.nom_lib = "Hola"

def limpiar_pant():
    for a in range(30):
        print(" ")

# MAIN
if __name__ == "__main__":
    libro1 = Libro()        # instanciar
    libro2 = Libro()
    libro3 = Libro()

    usuario1 = Usuario()
    usuario2 = Usuario()
    usuario3 = Usuario()

    servicio1 = Servicio()
    servicio2 = Servicio()
    servicio3 = Servicio()
    servicio4 = Servicio()

    s = Servicio()
    u = Usuario()
    l = Libro()

    datos_libros()
    # datos de los libros existentes
    datos_usuarios()
    # datos de los usuarios existentes
    datosServicios()
    # datos de los servicios asignados

    r = Revista()
    arrObjs = []  # vector de objetos
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
        print("    OPC 1: Mostrar usuarios                ")
        print("    OPC 2: NUEVOS  usuarios                ")
        print("                                           ")
        print("    OPC 3: Mostrar libros                  ")
        print("    OPC 4: NUEVOS libros                   ")
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
        elif opc == "1":                  # Opc 1 = Mostrar usuarios registrados
            print("            Usuarios del Sistema            ")
            u = usuario1
            print(u.mostrarUsuario())
            u = usuario2
            print(u.mostrarUsuario())
            u = usuario3
            print(u.mostrarUsuario())
            print()
        elif opc == "2":                  # Opc 2 = incluir nuevos usuarios
            print("            NUEVOS Usuarios               ")
            u.nuevoUsuario()       # agrega nuevo usuario
            print()
            print(u.mostrarUsuario())
            print()

        elif opc == "3":
            # Mostrar Libros registrados
            print("            Mostrar Libros             ")
            print()
            for j in range(3):
                print("Indice: ", j)
                print(arrObjs[j].autor, " ", arrObjs[j].titulo)

           ''' l = libro1
            print(l.mostrarLibro())
            l = libro2
            print(l.mostrarLibro())
            l = libro3
            print(l.mostrarLibro())
            print()'''

        elif opc == "4":
            print("            NUEVOS Libros               ")
            print()



            for i in range(3):
                x = str("obj") + str(i)
                x = Revista()
                x.setDatos()
                arrObjs.append(x)
                # print(f"Indice {i} dato {arrObjs[i].autor}")


            '''l.nuevoLibro()
            print()
            print(l.nuevoLibro())'''

        elif opc == "5":
            print("            Mostrar Servicios           ")
            print()
            s = servicio1
            print(s.mostrarServicio())
            s = servicio2
            print(s.mostrarServicio())
            s = servicio3
            print(s.mostrarServicio())
            s = servicio4
            print(s.mostrarServicio())
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
            matr1 = np.array([0,1,2,3])
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
