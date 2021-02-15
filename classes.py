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


class Cliente:
    def __init__(self, contador, nome, tel):
        self.id = contador
        self.nome = nome
        self.telefone = tel 
    
    def __str__(self):
        return f"----------------\nID: {self.id}\nNome: {self.nome}\nTelefone: {self.telefone}\n"


class Pedido:
    def __init__(self, contador, cliente, produtos, quantidades, valor):
        self.id = contador
        self.cliente = cliente
        self.produtos = [produtos]
        self.quantidades = [quantidades]
        self.valor = valor #[valor for produto,quantidade in zip(produtos,quantidades) valor = produto.preco * quantidade]
    
    def __str__(self):
        return f"----------------\nID: {self.id}\nCliente: {self.cliente.nome}\nValor: {self.valor}\n"
