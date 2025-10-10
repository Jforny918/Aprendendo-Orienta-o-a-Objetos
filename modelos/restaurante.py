class Restaurante: #definição de uma classe
    restaurantes = [] #todo restaurante que for criado através do método init será adicionado a essa lista
    def __init__(self, nome, categoria): #metodo construtor que inicializa os atributos, o self referencia o self que estamos criando)
        self._nome = nome.title() #atributo nome com a função Title que coloca a primeira letra de cada palavra em maiúscula
        self._categoria = categoria.upper() #atributo categoria com a função Upper que coloca todas as letras em maiúscula
        self._ativo = False #atributo ativo, o underline indica que é um atributo protegido que não deve ser acessado diretamente fora da classe
        Restaurante.restaurantes.append(self)

    def __str__(self): #metodo que retorna uma string representando o self
        return f'{self._nome} - {self._categoria} - {"Aberto" if self.ativo else "Fechado"}'
    
    @classmethod #decorador que indica que o metodo é de classe e não de instancia
    def listar_restaurantes(cls): #metodo criado para listar os restaurantes
        for restaurante in cls.restaurantes:
            print (f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | Status')
            print ('-'*60)
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {"Aberto" if restaurante.ativo else "Fechado"}')
            print ()

    @property #decorador que transforma o metodo em um atributo
    def ativo (self):
        return 'Verdadeiro' if  self._ativo else 'Falso' #retorna o valor do atributo ativo
    
    def alternar_estado (self): #metodo que altera o estado do restaurante
        self._ativo = not self._ativo #alterna o valor do atributo ativo entre True e False
        

restaurante_praca = Restaurante('praça', 'Gourmet') #instancia de um self
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('pizza express', 'Italiana') #instancia de um self

Restaurante.listar_restaurantes()


