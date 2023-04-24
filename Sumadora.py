
import tkinter as tk

def Sumar():
    suma = int(valor1.get()) + int(valor2.get())
    return vari.set(suma)

def Salir():
    vent.destroy()

def Ventana():
    print()
    print("+++++++++++++++++++++++++++++++++++++++++++")
    vent = tk.Tk()
    vent.title(" S U M A D O R A ")
    vent.geometry("380x300")  # definir tamaño de la ventana ancho x alto
    vent.configure(background="dark turquoise")
    vari = tk.StringVar()

    lbl_titulo = tk.Label(vent, text="Ingrese el primer valor")
    lbl_titulo.pack(padx=10, pady=10)
    valor1 = tk.Entry(vent)
    valor1.pack(fill=tk.X, padx=5, pady=5, ipadx=5, ipady=5)

    lbl_titulo = tk.Label(vent, text="Ingrese el segundo valor")
    lbl_titulo.pack(padx=10, pady=10)
    valor2 = tk.Entry(vent)
    valor2.pack(fill=tk.X, padx=5, pady=5, ipadx=5, ipady=5)

    btnSuma = tk.Button(vent, text="Resultado", fg="blue", command=Sumar)
    btnSuma.pack(side=tk.TOP)
    result = tk.Label(vent, bg="plum", textvariable=vari, padx=5, pady=5, width=50)
    result.pack()

    btnSalir = tk.Button(vent, text="S A L I R ", fg="blue", command=Salir)
    btnSalir.pack(side=tk.TOP)

    vent.mainloop()
