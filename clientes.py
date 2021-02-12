class Cliente:
    def __init__(self, contador, nome, tel):
        self.id = contador
        self.nome = nome
        self.telefone = tel 
    
    def __str__(self):
        return f"----------------\nID: {self.id}\nNome: {self.nome}\nTelefone: {self.telefone}\n"


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


clientes = []
clientes = cadastrar_clientes(clientes)
visualizar_clientes(clientes)