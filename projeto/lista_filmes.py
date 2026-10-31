import urllib.request
import json


def resultado_filme(tipo):
    print('caiu aqui')
    if tipo == 'Populares':
        url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=2dd85411d761b363a1c36f566d290b69'
    elif tipo == '2010':
        url= 'https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=2dd85411d761b363a1c36f566d290b69'
    elif tipo == 'Animação':
        url ='https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=2dd85411d761b363a1c36f566d290b69'
    response = urllib.request.urlopen(url)

    dados = response.read()

    dados_json = json.loads(dados)

        
    return dados_json['results']
