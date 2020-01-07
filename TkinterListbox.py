# Solicitar el ingreso del nombre de una persona y seleccionar de un control Listbox un país.
# Al presionar un botón mostrar en la barra de la ventana el nombre ingresado y el país seleccionado.

import tkinter

class app6:

	def __init__(self):

		self.ventana=tkinter.Tk()
		self.ventana.title("Nombre y Nacionalidad")
		self.nombre=tkinter.StringVar()
		self.etiqueta=tkinter.Label(self.ventana,text="Ingrese el nombre: ")
		self.etiqueta.grid(column=0,row=0)
		self.ingresonombre=tkinter.Entry(self.ventana,width=20,textvariable=self.nombre)
		self.ingresonombre.grid(column=1,row=0)
		self.etiqueta2=tkinter.Label(self.ventana,text="Ingrese Nacionalidad")
		self.etiqueta2.grid(column=0,row=1)
		self.paises=tkinter.Listbox(self.ventana)
		self.paises.grid(column=0,row=2)
		self.paises.insert(0,"Argentina")
		self.paises.insert(1,"Brasil")
		self.paises.insert(2,"China")
		self.paises.insert(3,"Otros")
		self.botoningreso=tkinter.Button(self.ventana,text="Ingresar",command=self.ingresar)
		self.botoningreso.grid(column=0,row=3)
		self.ventana.mainloop()

	def ingresar(self):

		self.ventana.title(self.nombre.get()+" "+self.paises.get(self.paises.curselection()[0]))



