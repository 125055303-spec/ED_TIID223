def calcular_promedio(calificaciones):
	if not calificaciones:
		raise ValueError("Debe ingresar al menos una calificación.")
	return sum(calificaciones) / len(calificaciones)


try:
	cantidad = int(input("¿Cuántas calificaciones desea ingresar? "))
	if cantidad <= 0:
		raise ValueError("La cantidad debe ser mayor que cero.")

	calificaciones = [
		float(input(f"Ingrese la calificación {i + 1}: "))
		for i in range(cantidad)
	]
	print(f"El promedio es: {calcular_promedio(calificaciones):.2f}")
except ValueError as error:
	print(f"Entrada no válida: {error}")
