#se importa la libreria de tkinter con todas sus funciones 
from tkinter import *


#.....................
# funciones de la app
#.....................


#.....................
# ventana principal
#.....................

# se declara una variable llamada ventana principal, que adquiere las caracteristicas de un objeto Tk ()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Sistemas UIS Socorro")

# tamaño de la ventana
ventana_principal.geometry("500x500")

# deshabilitar boton de minimizar
ventana_principal.resizable(0,0)

# color de fondo de la ventana
ventana_principal.config(bg="white")

#----------------------------
# frame entrada datos
# ----------------------------

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="yellow" , width=500, height=250)
frame_entrada.place(x=0, y=0)

#----------------------------
# frame operaciones
# ----------------------------

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="blue" , width=500, height=125)
frame_operaciones.place(x=0, y=250)


#----------------------------
# frame resultados
# ----------------------------

frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="red" , width=500, height=250)
frame_resultados.place(x=0, y=375)


# run
# se ejecuta la funcion (metodo) mainloop()de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega una ventana simple en la pantalla y queda a la espera de lo que el usuario haga. Cada accion del usuario se conoce como evento. El mainloop() es un bucle infinito.
ventana_principal.mainloop()