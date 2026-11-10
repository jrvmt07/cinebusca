class Filme:
    def __init__(self, titulo, ano, genero, nota, sinopse, plataformas):
        self.titulo = titulo
        self.ano = ano
        self.genero = genero
        self.nota = nota
        self.sinopse = sinopse
        self.plataformas = plataformas

    def exibir_informacoes(self):
        print(f"Título: {self.titulo}")
        print(f"Ano: {self.ano}")
        print(f"Gênero: {self.genero}")

        if self.nota is None:
            print("Nota: Não disponível.")
        else:
            print(f"Nota: {self.nota}")

        print(f"Sinopse: {self.sinopse}")
        
        if self.plataformas:
            print(f"Onde assistir: {', '.join(self.plataformas)}")
        else:
            print("Onde assistir: Nenhuma plataforma encontrada.")