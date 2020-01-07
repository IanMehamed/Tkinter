import tkinter

class app2:

	def __init__(self):
		self.ventana=tkinter.Tk()
		self.ventana.title("Hola Madre e Hija!")
		self.boton1=tkinter.Button(self.ventana,text="Hija",command=self.titulosara)
		self.boton1.grid(column=1,row=0)
		self.boton2=tkinter.Button(self.ventana,text="Madre",command=self.titulosofi)
		self.boton2.grid(column=4,row=0)
		self.ventana.mainloop()

	def titulosara(self):
		self.ventana.title("Hola Sarita!")

	def titulosofi(self):
		self.ventana.title("Hola Sofi!")


		



# Disponer dos objetos de la clase Button con las etiquetas: "varón" y "mujer", 
# al presionarse mostrar en la barra de títulos de la ventana la etiqueta del botón presionado.