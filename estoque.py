class Produto:
    def __init__(self, contador, nome, quantidade, preco):
        self.id = contador
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
    
    def __str__(self):
        return f"----------------\nID: {self.id}\nNome: {self.nome}\nQuantidade: {self.quantidade}\nPreço: {self.preco}"

    def adicionar(self, quantidade):
        self.quantidade += quantidade

    def remover(self, quantidade):
        self.quantidade -= quantidade

    def alterar_preco(self, preco):
        self.preco = preco


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


def editar_produtos(produtos, opcaoSecundaria, opcaoMensagem):
        print("Estes são os produtos disponiveis:\n")
        visualizar_produtos(produtos)
        mensagemIdProduto = opcaoMensagem[opcaoSecundaria][0]
        mensagemQuantidade = opcaoMensagem[opcaoSecundaria][1]
        IdProduto = int(input(mensagemIdProduto))
        quantidade = int(input(mensagemQuantidade))
        
        for i, produto in enumerate(produtos):
            if i == IdProduto:
                if opcaoSecundaria == "2":
                    produto.adicionar(quantidade)
                    break
                elif opcaoSecundaria == "3":
                    produto.remover(quantidade)
                    break
                elif opcaoSecundaria == "4":
                    produto.alterar_preco(quantidade)
                    break


def visualizar_produtos(produtos):
    for produto in produtos:
        print(produto)
    print("----------------")

opcaoMensagem = {
    "2": ("Insira o ID do produto que deseja alterar: ", "Insira a quantidade que deseja adicionar: "),
    "3": ("Insira o ID do produto que deseja alterar: ", "Insira a quantidade que deseja remover: "),
    "4": ("Insira o ID do produto que deseja alterar: ", "Insira o novo preço do produto: ")
}
produtos = []
opcaoPrincipal = "x"

while opcaoPrincipal != "n":
    print("deseja:\n1- Cadastrar novo produto\n2- Adicionar ao estoque\n3- Remover do estoque\n4- Alterar preço")
    opcaoSecundaria = input()

    if opcaoSecundaria == "1":
        produtos = cadastrar_produtos(produtos)

    else:
        editar_produtos(produtos, opcaoSecundaria, opcaoMensagem)

    print("\n")
    visualizar_produtos(produtos)
    opcaoPrincipal = input("Deseja realizar outra ação? (s/n):" )

visualizar_produtos(produtos)


