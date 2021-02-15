from classes import Produto, Cliente, Pedido
from clientes import interface_clientes
from estoque import interface_produtos
from pedidos import cadastrar_pedidos


clientes = []
produtos = []
pedidos = []
opcaoPrincipal = "x"
opcaoMensagem = {
    "2": ("Insira o ID do produto que deseja alterar: ", "Insira a quantidade que deseja adicionar: "),
    "3": ("Insira o ID do produto que deseja alterar: ", "Insira a quantidade que deseja remover: "),
    "4": ("Insira o ID do produto que deseja alterar: ", "Insira o novo preço do produto: ")
}
opcaoMenu = "x"

while opcaoMenu != "4":
    print("Deseja:\n1- Clientes\n2- Estoque\n3- Pedidos\n4- Sair")
    opcaoMenu = input()
    if opcaoMenu == "1":
        interface_clientes(clientes)
    elif opcaoMenu == "2":
        interface_produtos(produtos, opcaoMensagem)
    elif opcaoMenu == "3":
        pedidos = cadastrar_pedidos(pedidos, clientes, produtos)
        print("----------------\nPedidos:")
        for pedido in pedidos:
            print(pedido)
        print("----------------")