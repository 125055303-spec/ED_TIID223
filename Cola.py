from collections import deque

cola=deque (["Ana","Carlos"])
cola.append("Jorge")
cola.append("Andres")
print("Cola actual:", cola)

atendido=cola.popleft()
print(f"Se atendió a:{atendido}")

print("Cola restante:",cola)

atendido=cola.popleft()
print(f"Se atendió a:{atendido}")

print("Cola restante:",cola)
