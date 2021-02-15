from classes import Produto


def interface_produtos(produtos, opcaoMensagem):
    opcaoProdutos = "x"
    while opcaoProdutos != "6":
        print("Deseja:\n1- Cadastrar novo produto\n2- Adicionar ao estoque\n3- Remover do estoque\n4- Alterar preço\n5- Visualizar Produtos\n6- Sair")
        opcaoProdutos = input()
        if opcaoProdutos == "1":
            produtos = cadastrar_produtos(produtos)
        elif opcaoProdutos == "5":
            visualizar_produtos(produtos)
        elif opcaoProdutos != "6":
            editar_produtos(produtos, opcaoProdutos, opcaoMensagem)


def cadastrar_produtos(produtos):
    continuar = "y"
    while continuar != "n":
        nome = str(input("Digite o nome do produto: "))
        quantidade = int(input("Digite a quantidade ja existente: "))
        preco = float(input("Digite o preço do produto: "))
        produto = Produto(len(produtos), nome, quantidade, preco)
        produtos.append(produto)
        continuar = input("deseja continuar? (y / n): ")
    return produtos


def editar_produtos(produtos, opcaoProdutos, opcaoMensagem):
        print("Estes são os produtos disponiveis:\n")
        visualizar_produtos(produtos)
        mensagemIdProduto = opcaoMensagem[opcaoProdutos][0]
        mensagemQuantidade = opcaoMensagem[opcaoProdutos][1]
        IdProduto = int(input(mensagemIdProduto))
        quantidade = float(input(mensagemQuantidade))
        for i, produto in enumerate(produtos):
            if i == IdProduto:
                if opcaoProdutos == "2":
                    produto.adicionar(int(quantidade))
                    break
                elif opcaoProdutos == "3":
                    produto.remover(int(quantidade))
                    break
                elif opcaoProdutos == "4":
                    produto.alterar_preco(quantidade)
                    break


def visualizar_produtos(produtos):
    for produto in produtos:
        print(produto)
    print("----------------")