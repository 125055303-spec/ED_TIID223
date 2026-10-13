matriz=[
    [73,12,89,34],
    [45,67,23,90],
    [56,80,12,34]
]
for i in matriz:
    if 80 in i:
        print(f"El valor 80 se encuentra en la fila {i}")
        break

for fila in matriz:
    for numero in fila:
        if numero==80:
            print(f"El valor 80 se encuentra en la fila {fila}")
