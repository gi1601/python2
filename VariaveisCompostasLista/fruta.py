fruta = ["Maça", "Banana", "Uva", "Abacaxi"]
fruta[3]="Melancia"
fruta.append("Laranja")
fruta.insert(1,"Morango")

#deletar
del fruta[3]
fruta.pop(3)
fruta.remove("Banana")

#verificar se tem um elemento

if "Abacaxi" in fruta:
    fruta.remove("Abacaxi")
else:
    print("Não encontrado")

print(fruta)