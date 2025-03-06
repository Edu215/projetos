from cliente import Cliente  # Import corrigido para "Cliente"
from produto import Produto

if __name__ == "__main__":
    # Criando um cliente
    cliente = Cliente(id_cliente=1, nome="João Silva", idade=30, genero="Masculino")
    cliente.estabelecer_perfil({'esportes': 5, 'tecnologia': 3, 'moda': 2})

    # Criando um produto
    produto = Produto(id_produto=101, nome="Tênis Esportivo", categoria="Esportes", preco=199.99)

    # Registrando uma interação
    contexto = {'local': 'online', 'horario': 'noite'}
    cliente.registrar_interacao(produto, contexto)

    # Atualizando preferências
    cliente.atualizar_preferencias({'esportes': 6})

    # Exibindo informações
    print(cliente)
    print(produto)