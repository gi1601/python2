nota = 0
qtd = 0
while True:
    n= float(input("Digite uma nota:"))
    qtd+= 1
    nota+= n
    if n < 0:
        media = nota/qtd
        print("A média é ", media)
        break
    f = str(input("Deseja continuar?[S/N]:"))
    if f == "N":
        media = nota/qtd
        print("A média é ", media)
        break

