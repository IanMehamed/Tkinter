
# Confeccionar un programa que permita ingresar dos números en controles de tipo Entry, luego sumar los 
# dos valores ingresados y mostrar la suma en una Label al presionar un botón.
import tkinter

class app3:

	def __init__(self):

		self.ventana=tkinter.Tk()
		self.presentacion=tkinter.Label(self.ventana,text="Este programa está diseñado para resolver una suma entre dos numeros")
		self.presentacion.grid(column=0,row=0)
		self.etiqueta1=tkinter.Label(self.ventana,text="Ingrese un número: ")
		self.etiqueta1.grid(column=0,row=1)
		self.etiqueta1=tkinter.Label(self.ventana,text="Ingrese otro número: ")
		self.etiqueta1.grid(column=0,row=2)
		self.dato1=tkinter.StringVar()
		self.dato2=tkinter.StringVar()
		self.entrada1=tkinter.Entry(self.ventana,width=10,textvariable=self.dato1)
		self.entrada1.grid(column=1,row=1)
		self.entrada2=tkinter.Entry(self.ventana,width=10,textvariable=self.dato2)
		self.entrada2.grid(column=1,row=2)
		self.calcular=tkinter.Button(self.ventana,text="Calcular",command=self.sumar)
		self.calcular.grid(column=0,row=3)
		self.resultado=tkinter.Label(self.ventana,text="Resultado: ")
		self.resultado.grid(column=0,row=4)
		self.ventana.mainloop()

	def sumar(self):
		a=int(self.dato1.get())
		b=int(self.dato2.get())
		suma=a+b
		self.resultado.config(text="Resultado: "+str(suma))


