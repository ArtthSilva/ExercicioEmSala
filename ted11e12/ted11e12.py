import csv

def maiorPublicoDeFilmes(filmes):
    cabecalho = next(filmes)
    totalPublico = 0
    nomeDoFilme = ''
    anoDeExibicao = ''

    for i, filme in enumerate(filmes):
        coluna = float(filme[9])

        if coluna > totalPublico:
            totalPublico = coluna
            nomeDoFilme = filme[2]
            anoDeExibicao = filme[1]
        else:
            continue

    print('O filme com maior publico é  ', nomeDoFilme)
    print('Total do publico ', totalPublico)
    print('Ano de exibição  ', anoDeExibicao)
    



with  open('filmes.csv', newline='', encoding='utf-8') as filmes:
    lerFilmes = csv.reader(filmes)

    maiorPublicoDeFilmes(lerFilmes)
