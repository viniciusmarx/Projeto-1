# Gerar relatório do estoque atual
def relatorio_estoque():
    tabela = pd.read_csv("estoque.csv")
    file = open("Relatório de Estoque.txt", "w")
    file.write("Relatório atual do estoque.\n")
    lista_de_produtos = tabela["produto"].tolist()
    lista_de_quantidades = tabela["estoque"].tolist()
    for x in range(0, len(lista_de_produtos)):
        file.write("O item '{}' tem uma quantidade de {} unidades.\n".format(
            lista_de_produtos[x], lista_de_quantidades[x]))

    file.close()


# Gerar relatório de produtos mais comprados
def relatorioMaisComprado():
    tabela = pd.read_csv("estoque.csv")
    file = open("Relatório de Compra.txt", "w")
    file.write("Relatório de produto mais comprado.\n")
    # ordena tabela decrescentemente pela coluna compras, depois de ordenar pega o primeiro valor da coluna produto pelo index
    produto_maior = tabela.sort_values(
        by="compras", ascending=False)["produto"][0]
    maior_compra = tabela.sort_values(
        by="compras", ascending=False)["compras"][0]
    file.write("O item '{}' tem uma quantidade de {} unidades.\n".format(
        produto_maior, maior_compra))

    file.close()


# Função para exibir o menu
def exibir_menu():
    print("===== OPÇÕES =====")
    print("1. Cadastrar produto")
    print("2. Cadastrar compra de produto")
    print("3. Alterar quantidade de produtos no estoque")
    print("4. Consultar quantidade do produto")
    print("5. Consultar preço do produto")
    print("6. Consultar valor total do estoque")
    print("7. Gerar gráfico da quantidade de produtos no estoque")
    print("8. Gerar gráfico de produtos mais comprados")
    print("9. Gerar relatório do estoque atual")
    print("10. Gerar relatório de produto mais comprado")
    print("0. Sair")


def main():
    seletor = 99
    while (seletor != 0):
        exibir_menu()
        seletor = int(input("Digite a opção desejada:"))
        if (seletor == 1):
            cadastrar_produtos()
            output.clear()

        elif (seletor == 2):
            cadastrar_compras()
            output.clear()

        elif (seletor == 3):
            alterar_quantidade_produtos()
            output.clear()

        elif (seletor == 4):
            consulta_estoque()
            input("Digite algo para continuar")
            output.clear()

        elif (seletor == 5):
            consulta_precos()
            input("Digite algo para continuar")
            output.clear()

        elif (seletor == 6):
            preco_total_estoque()
            input("Digite algo para continuar")
            output.clear()

        elif (seletor == 7):
            grafico_estoque()
            input("Digite algo para continuar")
            output.clear()

        elif (seletor == 8):
            grafico_compras()
            input("Digite algo para continuar")
            output.clear()

        elif (seletor == 9):
            relatorio_estoque()
            output.clear()
            print("Relatório salvo com sucesso!")

        elif (seletor == 10):
            relatorioMaisComprado()
            output.clear()
            print("Relatório salvo com sucesso!")

        elif (seletor == 0):
            output.clear()
            print("Programa finalizado!")
        else:
            output.clear()
            print("Número inválido")


main()
