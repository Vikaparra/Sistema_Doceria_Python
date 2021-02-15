from classes import Cliente


def interface_clientes(clientes):
    opcaoClientes = "x"
    while opcaoClientes != "3":
        print("Deseja:\n1- Cadastrar Cliente\n2- Visualizar Cliente\n3- Sair")
        opcaoClientes = input()
        if opcaoClientes == "1":
            clientes = cadastrar_clientes(clientes)
        elif opcaoClientes == "2":
            visualizar_clientes(clientes)


def cadastrar_clientes(clientes):
    continuar = "y"
    while continuar != "n":
        nome = str(input("Digite o nome do cliente: "))
        telefone = str(input("Digite o telefone do cliente: "))
        cliente = Cliente(len(clientes), nome, telefone)
        clientes.append(cliente)
        continuar = input("deseja continuar? (y / n): ")
    return clientes


def visualizar_clientes(clientes):
    for cliente in clientes:
        print(cliente)
    print("----------------")