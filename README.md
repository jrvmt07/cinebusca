🎬 CineBusca

Sistema de busca de filmes desenvolvido em Python, utilizando orientação a objetos e consumo de APIs.

O CineBusca permite pesquisar filmes pelo título e consultar informações como ano de lançamento, gênero, avaliação, sinopse e plataformas de streaming disponíveis no Brasil.

✨ Funcionalidades

🔎 Busca de filmes pelo título.

🎞️ Exibição dos filmes encontrados.

📅 Consulta do ano de lançamento.

🎭 Identificação dos gêneros.

⭐ Exibição da avaliação do filme.

📝 Consulta da sinopse.

📺 Identificação das plataformas de streaming disponíveis no Brasil.

🛠️ Tecnologias utilizadas

Python — linguagem principal.

FastAPI — desenvolvimento da API.

Requests — consumo de APIs HTTP.

TMDB API — obtenção dos dados dos filmes.

Render — hospedagem da API.

📂 Estrutura do projeto

cinebusca/
├── api.py
├── main.py
├── filme.py
├── consulta_filmes.py
├── requirements.txt
├── README.md
└── .gitignore

🚀 Como executar o projeto

1. Clone o repositório

git clone https://github.com/jrvmt07/cinebusca.git

2. Entre na pasta do projeto

cd cinebusca

3. Instale as dependências

pip install -r requirements.txt

4. Execute a aplicação

python main.py

Pronto! Agora é só pesquisar o filme desejado.

Observação: Não é necessário criar uma conta na TMDB nem configurar um token. O CineBusca utiliza uma API própria hospedada no Render, responsável por consultar e organizar os dados dos filmes.