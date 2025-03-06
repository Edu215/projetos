class Produto:
    def __init__(self, id_produto, nome, categoria, preco):
        self.id_produto = id_produto
        self.nome = nome
        self.categoria = categoria
        self.preco = preco

    def __str__(self):
        return f"Produto(ID: {self.id_produto}, Nome: {self.nome}, Categoria: {self.categoria}, Preço: {self.preco})"