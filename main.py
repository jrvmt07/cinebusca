from consulta_filmes import ConsultaFilmes

consulta = ConsultaFilmes()

filmes = consulta.buscar_filmes("Interestelar")

for filme in filmes:
    filme.exibir_informacoes()
    print("----------------------")