notas = {}
continuar = True

while continuar:
    nota = float(input("Informe uma nota: "))
    notas[len(notas) + 1] = nota

    resposta = input("Deseja continuar? (S/N): ")
    if resposta in "N":
        break

media = sum(notas.values()) / len(notas)
print("A média das notas é:", media)