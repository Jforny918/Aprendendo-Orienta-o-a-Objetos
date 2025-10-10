class musica:
    nome = ''
    artista = ''
    ano = 0

musica_favorita = musica ()
musica_favorita.nome = 'Imagine'
musica_favorita.artista = 'John Lennon'
musica_favorita.ano = 1971

musica_favorita_mae = musica()
musica_favorita_mae.nome = 'Fire for you'
musica_favorita_mae.artista = 'Cannons'
musica_favorita_mae.ano = 2019

musica_favorita_namorado = musica()
musica_favorita_namorado.nome = 'Anyone But You'
musica_favorita_namorado.artista = 'Still Woozy'
musica_favorita_namorado.ano = 2020

musicas = [musica_favorita, musica_favorita_mae, musica_favorita_namorado]
#é necessário criar uma lista para armazenar os objetos
print (vars(musicas[0]))
print (f'Música: {musicas[0].nome} - Artista: {musicas[0].artista} - Ano: {musicas[0].ano}')


