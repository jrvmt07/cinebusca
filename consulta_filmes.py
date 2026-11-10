import os
import requests
from dotenv import load_dotenv
from filme import Filme


class ConsultaFilmes:
    def __init__(self):
        load_dotenv()
        self.token = os.getenv("TMDB_TOKEN")

    def buscar_filmes(self, titulo):
        url = "https://api.themoviedb.org/3/search/movie"

        headers = {
            "Authorization": f"Bearer {self.token}",
            "accept": "application/json"
        }

        parametros = {
            "query": titulo,
            "language": "pt-BR"
        }

        resposta = requests.get(
            url,
            headers=headers,
            params=parametros
        )

        resposta.raise_for_status()

        dados = resposta.json()

        filmes = []

        for resultado in dados["results"]:
            titulo = resultado["title"]

            data_lancamento = resultado["release_date"]
            ano = data_lancamento[:4] if data_lancamento else "Não disponível"

            nota = resultado["vote_average"]

            sinopse = resultado["overview"] or "Sinopse não disponível"

            filme = Filme(
                titulo=titulo,
                ano=ano,
                genero="Não informado",
                nota=nota,
                sinopse=sinopse
            )

            filmes.append(filme)

        return filmes