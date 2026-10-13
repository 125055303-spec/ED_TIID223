#Crear una pila vacía 
historial=[]
#Apilar/Push (Agregar elementos)
historial.append("google.com")
historial.append("youtube.com")
historial.append("github.com")

print("Historial:",historial)

#Ver el elemento superior (Peek/cima)
pagina_actual=historial[2]
print("Página actual:",pagina_actual)

#Desapilar / Pop (Eliminar el último elemento ingresado)
pagina_salida=historial.pop()
print("Saliendo de:",pagina_salida)

print("Historial actualizado:", historial)