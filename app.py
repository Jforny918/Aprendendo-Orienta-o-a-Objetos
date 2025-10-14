from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante ('praca', 'gourmet')
bebida_suco = Bebida ('Suco de Laranja', 5.00, '300ml')
prato_bife = Prato ('Bife a cavalo', 25.00, 'Bife a cavalo com arroz, feijão e batata frita')
bebida_agua = Bebida ('Água sem gás', 3.00, '500ml')
prato_strogonoff = Prato ('Strogonoff de frango', 30.00, 'Strogonoff de frango com arroz branco e batata palha')

def main():
    print (bebida_suco)
    print (prato_bife)

if __name__ == '__main__':
    main()