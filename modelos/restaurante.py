from modelos.avaliacao import Avaliacao #importa a classe Avaliacao do arquivo avaliacao.py

class Restaurante: #definição de uma classe
    restaurantes = [] #todo restaurante que for criado através do método init será adicionado a essa lista
    def __init__(self, nome, categoria): #metodo construtor que inicializa os atributos, o self referencia o self que estamos criando)
        self._nome = nome.title() #atributo nome com a função Title que coloca a primeira letra de cada palavra em maiúscula
        self._categoria = categoria.upper() #atributo categoria com a função Upper que coloca todas as letras em maiúscula
        self._ativo = False #atributo ativo, o underline indica que é um atributo protegido que não deve ser acessado diretamente fora da classe
        self._avaliacao = [] #atributo avaliação que é uma lista vazia
        Restaurante.restaurantes.append(self)

    def __str__(self): #metodo que retorna uma string representando o self
        return f'{self._nome} - {self._categoria} - {"Aberto" if self.ativo else "Fechado"}'
    
    @classmethod #decorador que indica que o metodo é de classe e não de instancia
    def listar_restaurantes(cls): #metodo criado para listar os restaurantes
        print('Nome do Restaurante'.ljust(25), '|', 'Categoria'.ljust(25), '|', 'Avaliação'.ljust(25), '| Status')
        for restaurante in cls.restaurantes:
           print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {'Aberto' if restaurante.ativo == 'Verdadeiro' else 'Fechado'}")

           

    @property #decorador que transforma o metodo em um atributo
    def ativo (self):
        return self._ativo
    
    def alternar_estado (self): #metodo que altera o estado do restaurante
        self._ativo = not self._ativo #alterna o valor do atributo ativo entre True e False
        

    def receber_avaliacao (self, cliente, nota): #metodo que recebe uma avaliação
        if 0 < nota <= 5:
            avaliacao = Avaliacao (cliente, nota) #cria uma instancia da classe Avaliacao
            self._avaliacao.append(avaliacao) #adiciona a avaliação na lista de avaliações do restaurante
        
    @property
    def media_avaliacoes (self): #metodo que lista as avaliacoes do restaurante
        if not self._avaliacao:
            return 'Sem avaliações' 
        media = sum (avaliacao._nota for avaliacao in self._avaliacao) #soma todas as notas das avaliações
        quantidade_notas = len(self._avaliacao) #conta a quantidade de avaliações
        media = media / quantidade_notas #calcula a media de avaliações
        return round (media, 1 ) #retorna a media arredondada

        
    