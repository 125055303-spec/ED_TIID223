
numeros=[10,20,30,40,50]

print(numeros[2])  # Imprime el tercer elemento de la lista
numeros[3]=15
print(numeros)  # Imprime la lista actualizada

numeros.append(60)  # Agrega un nuevo elemento al final de la lista
print(numeros)  # Imprime la lista después de agregar un nuevo elemento 

numeros.pop(1)  # Elimina el segundo elemento de la lista
print(numeros)  # Imprime la lista después de eliminar un elemento  

numeros.remove(30)  # Elimina el elemento con valor 30 de la lista
print(numeros)  # Imprime la lista después de eliminar el elemento con valor 30

frutas=["mango","manzana","uva","pera","Maracuya"]
frutas.remove("uva")  # Elimina el elemento "uva" de la lista
print(frutas)  # Imprime la lista después de eliminar "uva"

frutas.pop(3)  # Elimina el último elemento de la lista
print(frutas)  # Imprime la lista después de eliminar el último elemento

frutas.append("kiwi")  # Agrega un nuevo elemento "kiwi" al final de la lista
print(frutas)  # Imprime la lista después de agregar "kiwi"

frutas[2]="fresa"  # Cambia el tercer elemento de la lista a "fresa"
print(frutas)  # Imprime la lista después de cambiar el tercer elemento a "fresa"

arreglo=[]  # Crea un arreglo vacío
n=int(input("Ingrese el tamaño del arreglo: "))  # Solicita al usuario el tamaño del arreglo

arreglo[0]=int(input("Ingrese el primer elemento del arreglo: "))  # Solicita al usuario el primer elemento del arreglo
print(arreglo)  # Imprime el arreglo después de agregar el primer elemento

