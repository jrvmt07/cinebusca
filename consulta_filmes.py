
import requests
from filme import Filme


class ConsultaFilmes:
    def buscar_filmes(self, titulo):
        url = "https://cinebusca-api.onrender.com/filmes"

        resposta = requests.get(
            url,
            params={"titulo": titulo}
        )

        resposta.raise_for_status()

        dados = resposta.json()

        filmes = []

        for resultado in dados:
            filme = Filme(
                titulo=resultado["titulo"],
                ano=resultado["ano"],
                genero=resultado["genero"],
                nota=resultado["nota"],
                sinopse=resultado["sinopse"],
                plataformas=resultado["plataformas"]
            )

            filmes.append(filme)

        return filmes
