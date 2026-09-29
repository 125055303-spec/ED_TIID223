matriz=[
    [1,2,3],
    [4,5,7]
]
print ("Mostrar matriz")
for fila in matriz:
    print (fila)
""" Se muestra el número 6 """
print ("Mostrar el 6")
print (matriz[1][2])
""" Se muestra la fila y columna 0 """
print(matriz[0])
""" Modificar los valores dentro de la matriz """
matriz[1][1]=8
print ("Matriz modificada")
print (matriz)

matriz.append([7,8,9])  # Agrega una nueva fila a la matriz
print ("Matriz después de agregar una nueva fila")
print (matriz)

matriz[0].pop(2)  # Elimina el segundo elemento de la primera fila
print ("Matriz después de eliminar el tercer elemento de la primera fila")
print (matriz)

""" Primer exposición sobre  matriz """