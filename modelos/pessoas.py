class Pessoas:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'
    
    def saudacao(self):
        if self.profissao:
            return f'Olá, meu nome é {self.nome}, tenho {self.idade} anos e sou {self.profissao}.'
        else:
            return f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.'
    def aniversario (self):
        self.idade += 1
        print (f'Parabéns, {self.nome}! Você agora tem {self.idade} anos!')

pessoa1 = Pessoas('Júlia', 21, 'Desenvolvedora de Software')
print(pessoa1.saudacao())
pessoa1.aniversario() 
    

