
import os
import requests
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

TOKEN = os.getenv("TMDB_TOKEN")
BASE_URL = "https://api.themoviedb.org/3"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "accept": "application/json"
}


def buscar_generos():
    resposta = requests.get(
        f"{BASE_URL}/genre/movie/list",
        headers=HEADERS,
        params={"language": "pt-BR"}
    )
    resposta.raise_for_status()

    return {
        genero["id"]: genero["name"]
        for genero in resposta.json()["genres"]
    }


def buscar_provedores(id_filme):
    resposta = requests.get(
        f"{BASE_URL}/movie/{id_filme}/watch/providers",
        headers=HEADERS
    )
    resposta.raise_for_status()

    brasil = resposta.json()["results"].get("BR", {})
    provedores = brasil.get("flatrate", [])

    return [
        provedor["provider_name"]
        for provedor in provedores
    ]


@app.get("/filmes")
def buscar_filmes(titulo: str):
    if not TOKEN:
        raise HTTPException(
            status_code=500,
            detail="Token da TMDB não configurado."
        )

    resposta = requests.get(
        f"{BASE_URL}/search/movie",
        headers=HEADERS,
        params={
            "query": titulo,
            "language": "pt-BR"
        }
    )

    resposta.raise_for_status()

    dados = resposta.json()
    mapa_generos = buscar_generos()

    filmes = []

    for resultado in dados["results"]:
        data = resultado["release_date"]

        ids_generos = resultado["genre_ids"]

        generos = [
            mapa_generos[id_genero]
            for id_genero in ids_generos
            if id_genero in mapa_generos
        ]

        filme = {
            "titulo": resultado["title"],
            "ano": data[:4] if data else "Não disponível",
            "genero": ", ".join(generos) if generos else "Não informado",
            "nota": resultado["vote_average"],
            "sinopse": resultado["overview"] or "Sinopse não disponível",
            "plataformas": buscar_provedores(resultado["id"])
        }

        filmes.append(filme)

    return filmes
