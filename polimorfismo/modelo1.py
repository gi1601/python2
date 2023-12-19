class Profissao:
    def Acao(self):
        pass
class Estudante(Profissao):
    def Acao(self):
        print("Estudando..")

Aluno1 = Estudante()
Aluno1.Acao()

