num = int(input("Informe um número:"))
if num == 1:
    print("Amarelo")
elif num == 2:
    print("Azul")
elif num == 3:
    print("Verde")
else:
    print("Sem cor")

login =str(input("Digite seu login"))
senha =str(input("Digite seua senha"))
match(login,senha):
    case("Bruno", "1,2,3"):
        print("Logado com sucesso")
    case _:
        print(("login ou senha incorreto"))