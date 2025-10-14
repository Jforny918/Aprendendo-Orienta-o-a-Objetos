class Avaliacao:
    def __init__ (self, cliente, nota):
        self._cliente = cliente #o underline indica que é um atributo protegido que não deve ser acessado diretamente fora da classe
        self._nota = nota
