class functions:

	def __init__(self,x,y,w):
		self.menor = x
		self.mayor = y
		self.salto = w
		self.rango = range(self.menor, self.mayor, self.salto)

	def sum(self):
		suma = 0
		for i in self.rango:
			suma = suma + i
		return suma

print("ingrese el número menor")
menor = int(input())
print("ingrese el número mayor")
mayor = int(input())
print("ingrese el valor de los saltos")
saltos = int(input())

calcular = functions(menor, mayor, saltos)
print(calcular.sum())
