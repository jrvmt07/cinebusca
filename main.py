from consulta_filmes import ConsultaFilmes
permissao = True
print("==============================")
print("         🎬 CINEBUSCA")
print("==============================")
print("Encontre filmes e descubra onde assistir!")
print()
print("Olá, qual filme você deseja pesquisar?")
consulta = ConsultaFilmes()

while permissao:
    entrada = str(input())
    filmes = consulta.buscar_filmes(entrada)

    if filmes:
        print("\n===== FILMES ENCONTRADOS =====")

        for indice, filme in enumerate(filmes, start=1):
            print(f"{indice}. {filme.titulo} ({filme.ano})")

        escolha = int(input("\nDigite o número do filme desejado: "))

        if 1 <= escolha <= len(filmes):
            filme_escolhido = filmes[escolha - 1]

            print("\n===== FILME SELECIONADO =====")
            filme_escolhido.exibir_informacoes()

        else:
            print("Opção inválida!")


    else:
        print("Nenhum filme encontrado.")

    comando = input("\nDeseja pesquisar outro filme? (S/N): ").strip().lower()

    if comando == "s":
        print()
        print("qual filme você deseja pesquisar agora?")
        permissao = True
    else:
        print()
        print("Foi um prazer lhe ajudar, volte sempre!")
        permissao = False
