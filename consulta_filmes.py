import os
import requests
import unicodedata
import re
from dotenv import load_dotenv
from filme import Filme


class ConsultaFilmes:
    def __init__(self):
        load_dotenv()
        self.token = os.getenv("TMDB_TOKEN")

    def normalizar_texto(self, texto):
        texto = texto.lower()

        texto = unicodedata.normalize("NFD", texto)
        texto = "".join(
        caractere for caractere in texto
        if unicodedata.category(caractere) != "Mn"
        )

        texto = re.sub(r"[^a-z0-9\s]", " ", texto)

        return " ".join(texto.split())

    def buscar_generos(self):
        url = "https://api.themoviedb.org/3/genre/movie/list"

        headers = {
            "Authorization": f"Bearer {self.token}",
            "accept": "application/json"
        }

        parametros = {
            "language": "pt-BR"
        }

        resposta = requests.get(
            url,
            headers=headers,
            params=parametros
        )

        resposta.raise_for_status()

        return resposta.json()

    def criar_mapa_generos(self):
        dados = self.buscar_generos()

        mapa_generos = {}

        for genero in dados["genres"]:
            id_genero = genero["id"]
            nome_genero = genero["name"]

            mapa_generos[id_genero] = nome_genero

        return mapa_generos
    
    def buscar_provedores(self, id_filme):
        url = f"https://api.themoviedb.org/3/movie/{id_filme}/watch/providers"

        headers = {
            "Authorization": f"Bearer {self.token}",
            "accept": "application/json"
        }

        resposta = requests.get(
            url,
            headers=headers
        )

        resposta.raise_for_status()

        dados = resposta.json()

        brasil = dados["results"].get("BR", {})

        provedores = brasil.get("flatrate", [])

        plataformas = []

        for provedor in provedores:
            plataformas.append(provedor["provider_name"])

        return plataformas

    def buscar_filmes(self, titulo):
        url = "https://api.themoviedb.org/3/search/movie"

        headers = {
            "Authorization": f"Bearer {self.token}",
            "accept": "application/json"
        }
        titulo_pesquisado = self.normalizar_texto(titulo)
        parametros = {
            "query": titulo_pesquisado,
            "language": "pt-BR"
        }

        resposta = requests.get(
            url,
            headers=headers,
            params=parametros
        )

        resposta.raise_for_status()

        dados = resposta.json()

        mapa_generos = self.criar_mapa_generos()

        filmes = []

        for resultado in dados["results"]:
            titulo = resultado["title"]

            data_lancamento = resultado["release_date"]
            ano = data_lancamento[:4] if data_lancamento else "Não disponível"

            nota = resultado["vote_average"]

            sinopse = resultado["overview"] or "Sinopse não disponível"

            ids_generos = resultado["genre_ids"]

            nomes_generos = []

            for id_genero in ids_generos:
                nome = mapa_generos.get(id_genero)

                if nome:
                    nomes_generos.append(nome)

            genero = ", ".join(nomes_generos) if nomes_generos else "Não informado"

            plataformas = self.buscar_provedores(resultado["id"])

            filme = Filme(
                titulo=titulo,
                ano=ano,
                genero=genero,
                nota=nota,
                sinopse=sinopse,
                plataformas=plataformas

            )

            filmes.append(filme)

        return filmes