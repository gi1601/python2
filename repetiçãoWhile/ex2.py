par= 0
while True:
    i= int(input("Digite um número positivo ou 0 para parar: "))
    if i % 2 ==0:
        par+= i
    if i == 0:
        print("Soma dos números pares é", par)
        break