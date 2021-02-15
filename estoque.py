class Estoque:
    def __init__(self, contador, nome, quantidade, preco):
        self.id = contador
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
    
    def __str__(self):
        return f"----------------\nID: {self.id}\nNome: {self.nome}\nQuantidade: {self.quantidade}\nPreço: {self.preco}"

    def adicionar(self, quantidade):
        self.quantidade = self.quantidade + quantidade

    def remover(self, quantidade):
        self.quantidade = self.quantidade - quantidade

    def alterar_preco(self, preco):
        self.preco = preco


def cadastrar_produtos(produtos):
    continuar = "y"
    while continuar != "n":
        nome = str(input("Digite o nome do produto: "))
        quantidade = int(input("Digite a quantidade ja existente: "))
        preco = float(input("Digite o preço do produto: "))
        produto = Estoque(len(produtos), nome, quantidade, preco)
        produtos.append(produto)
        continuar = input("deseja continuar? (y / n): ")
    return produtos


def visualizar_produtos(produtos):
    for produto in produtos:
        print(produto)
    print("----------------")

produtos = []
opcaoPrincipal = "x"

while opcaoPrincipal != "n":
    print("deseja:\n1- Cadastrar novo produto\n2- Adicionar ao estoque\n3- Remover do estoque\n4- Alterar preço")
    opcaoSecundaria = input()

    if opcaoSecundaria == "1":
        produtos = cadastrar_produtos(produtos)

    elif opcaoSecundaria == "2":
        print("Estes são os produtos disponiveis:\n")
        visualizar_produtos(produtos)
        IdProduto = int(input("Insira o ID do produto que deseja alterar: "))
        quantidade = int(input("Insira a quantidade do produto que deseja adicionar: "))
        
        for i, produto in enumerate(produtos):
            if i == IdProduto:
                produto.adicionar(quantidade)
                break

    elif opcaoSecundaria == "3":
        print("Estes são os produtos disponiveis:\n")
        visualizar_produtos(produtos)
        IdProduto = int(input("Insira o ID do produto que deseja alterar: "))
        quantidade = int(input("Insira a quantidade do produto que deseja remover: "))
        
        for i, produto in enumerate(produtos):
            if i == IdProduto:
                produto.remover(quantidade)
                break

    elif opcaoSecundaria == "4":
        print("Estes são os produtos disponiveis:\n")
        visualizar_produtos(produtos)
        IdProduto = int(input("Insira o ID do produto que deseja alterar: "))
        preco = int(input("Insira o novo preço do produto: "))

        for i, produto in enumerate(produtos):
            if i == IdProduto:
                produto.alterar_preco(preco)
                break 

    print("\n")
    visualizar_produtos(produtos)
    opcaoPrincipal = input("Deseja realizar outra ação? (s/n):" )

visualizar_produtos(produtos)


