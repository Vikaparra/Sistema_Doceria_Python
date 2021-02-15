from classes import Pedido
from clientes import visualizar_clientes
from estoque import visualizar_produtos


def cadastrar_pedidos(pedidos, clientes, produtos):
    continuar = "y"

    while continuar != "n":
        escolhaProdutos = "y"
        valor = 0
        listaProdutos = []
        listaQuantidades = []
        visualizar_clientes(clientes)
        idCliente = int(input("Digite o ID do cliente: "))
        for cliente in clientes:
            if cliente.id == idCliente:
                idCliente = cliente
                break
        while escolhaProdutos != "n":
            visualizar_produtos(produtos)
            idProduto = int(input("Digite o ID do produto desejado: "))
            quantidade = int(input("Digite a quantidade desejada: "))
            listaQuantidades.append(quantidade)
            for produto in produtos:
                if produto.id == idProduto:
                    listaProdutos.append(produto)
                    valor = valor + produto.preco * quantidade
                    break
            escolhaProdutos = input("Deseja escolher mais algum produto? ( y / n ): ")
        pedido = Pedido(len(pedidos), idCliente, listaProdutos, listaQuantidades, valor)
        pedidos.append(pedido)
        continuar = input("deseja cadastrar mais um pedido? (y / n): ")
    return pedidos