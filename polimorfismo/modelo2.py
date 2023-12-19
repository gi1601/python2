class Profissao:
    def Acao(self):
        return "A principal atividade é: "
class Estudante(Profissao):
    def Acao(self):
        print(super().Acao(),"Estudar")

Aluno1 = Estudante()
Aluno1.Acao()