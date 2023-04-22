
# Calcula lo adeudado por préstamo de libros o devoluciones atrasadas (morosidad)

def Calc():
    # Calculadora de multas por morocidad
    valor1 = 0
    valor2 = 0

    ctrl = " "
    while ctrl in ("s","S"):
        print("         CALCULADORA DEL SISTEMA ")
        print()
        ctrl2 = True
        while ctrl2:
            try:
                valor1 = float(input("==> Digite el PRIMER valor ==> "))
                oper = input("==> Digite la operación a realizar (+, -, *, /): ")
                valor2 = float(input("==> Digite el SEGUNDO valor ==> "))
            except:
                print("  Error en los datos ingresados  ")
                continue

        if oper in ["+", "-", "*", "/"]:
            print()
            result = Calc(valor1, valor2)   # calcular el resultado de la operación
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
        ctrl = input("===> Digite 'S' o 's' para finalizar o ENTER para continuar: ")
        limpiar_pant()
        clear()