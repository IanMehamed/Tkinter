# Mostrar los botones del 1 al 5. Cuando se presiona mostrar en una Label
# todos los botones presionados hasta ese momento

import tkinter

class app:
	def __init__(self):
		self.ventana=tkinter.Tk()
		self.ventana.title="Prueba"
		self.apretados=[]
		self.historial=tkinter.Label(self.ventana,text=self.apretados)
		self.historial.grid(column=0,row=0)
		self.boton1=tkinter.Button(self.ventana,text="Botón 1",command=self.apretar1)
		self.boton1.grid(column=0,row=1)
		self.boton2=tkinter.Button(self.ventana,text="Botón 2",command=self.apretar2)
		self.boton2.grid(column=1,row=1)
		self.boton3=tkinter.Button(self.ventana,text="Botón 3",command=self.apretar3)
		self.boton3.grid(column=2,row=1)
		self.boton4=tkinter.Button(self.ventana,text="Botón 4",command=self.apretar4)
		self.boton4.grid(column=3,row=1)
		self.boton5=tkinter.Button(self.ventana,text="Botón 5",command=self.apretar5)
		self.boton5.grid(column=4,row=1)
		self.ventana.mainloop()

	def apretar1(self):
		self.apretados.append("1")
		self.historial.config(text=self.apretados)

	def apretar2(self):
		self.apretados.append("2")
		self.historial.config(text=self.apretados)

	def apretar3(self):
		self.apretados.append("3")
		self.historial.config(text=self.apretados)

	def apretar4(self):
		self.apretados.append("4")
		self.historial.config(text=self.apretados)

	def apretar5(self):
		self.apretados.append("5")
		self.historial.config(text=self.apretados)
