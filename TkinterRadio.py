# Disponer tres controles de tipo Radiobutton con las etiquetas 'Rojo', 'Verde' y 'Azul'. 
# Cuando se presione un botón cambiar el color de fondo del formulario.
# Si consideramos que la variable ventana1 es un objeto de la clase Tk, luego si queremos 
# que el fondo sea de color rojo debemos llamar al método configure y en el parámetro bg indicar
#  un string con el color a activar ("red", "green" o "blue"):
#            self.ventana1.configure(bg="red")

import tkinter

class app5:
	
	def __init__(self):

		self.ventana=tkinter.Tk()
		self.intro=tkinter.Label(self.ventana,text="Cambiaremos el color de fondo!")
		self.intro.grid(column=0,row=0)
		self.seleccion=tkinter.IntVar()
		self.radiorojo=tkinter.Radiobutton(self.ventana,text="Rojo",variable=self.seleccion,value=1)
		self.radiorojo.grid(column=0,row=1)
		self.radioverde=tkinter.Radiobutton(self.ventana,text="Verde",variable=self.seleccion,value=2)
		self.radioverde.grid(column=0,row=2)
		self.radioazul=tkinter.Radiobutton(self.ventana,text="Azul",variable=self.seleccion,value=3)
		self.radioazul.grid(column=0,row=3)
		self.boton1=tkinter.Button(self.ventana,text="Cambiar Fondo",command=self.cambiarfondo)
		self.boton1.grid(column=1,row=4)
		self.ventana.mainloop()

	def cambiarfondo(self):

		a=self.seleccion.get()
		if a == 1:
			self.ventana.configure(bg="red")
		else:
			if a == 2:
				self.ventana.configure(bg="green")
			else:
				self.ventana.configure(bg="blue")


tomas=app5()