# Ingresar el nombre de usuario y clave en controles de tipo Entry. 
# Si se ingresa las cadena (usuario: juan, clave="abc123") luego mostrar en el título 
# de la ventana el mensaje "Correcto" en caso contrario mostrar el mensaje "Incorrecto".
# Para mostrar '*' cuando se ingresa la clave debemos pasar en el parámetro 'show' el caracter a mostrar:
#        self.entry2=tk.Entry(self.ventana1, width=30, textvariable=self.dato2, show="*")

#Ejercicio resuelto, para probar generar un objeto de la clase app4.

import tkinter

class app4:

	def __init__(self):

		self.ventana=tkinter.Tk()
		self.ventana.title("Aquí aparecerá el resultado del Loggin")
		self.usuario=tkinter.Label(self.ventana,text="Usuario: ")
		self.usuario.grid(column=0,row=0)
		self.contraseña=tkinter.Label(self.ventana,text="Contraseña: ")
		self.contraseña.grid(column=0,row=1)
		self.datousuario=tkinter.StringVar()
		self.datocontraseña=tkinter.StringVar()
		self.ingreso1=tkinter.Entry(self.ventana,width=10,textvariable=self.datousuario)
		self.ingreso1.grid(column=1,row=0)
		self.ingreso2=tkinter.Entry(self.ventana,width=10,textvariable=self.datocontraseña,show="*")
		self.ingreso2.grid(column=1,row=1)
		self.botonlog=tkinter.Button(self.ventana,text="Loguear",command=self.loguear)
		self.botonlog.grid(column=0,row=2)
		self.ventana.mainloop()

	def loguear(self):
		usuario=self.datousuario.get()
		contraseña=self.datocontraseña.get()
		if usuario == "juan" and contraseña =="abc123":
			self.ventana.title("Loggin Correcto!")
		else:
			self.ventana.title("Usuario o Contraseña Incorrecto..")

