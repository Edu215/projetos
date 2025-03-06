from cliente import Cliente
from produto import Produto

def main():
    
    print("Cadastro do Cliente")
    id_cliente = input("ID do Cliente: ")
    nome = input("Nome: ")
    idade = input("Idade: ")
    genero = input("Gênero: ")

    
    cliente = Cliente(id_cliente=id_cliente, nome=nome, idade=idade, genero=genero)

    
    print("\nEstabelecer Perfil do Cliente")
    interesses = {}
    while True:
        interesse = input("Digite um interesse (ou 'sair' para finalizar): ")
        if interesse.lower() == 'sair':
            break
        nivel_interesse = int(input(f"Nível de interesse em '{interesse}' (1 a 10): "))
        interesses[interesse] = nivel_interesse
    cliente.estabelecer_perfil(interesses)

    
    print("\nCadastro do Produto")
    id_produto = input("ID do Produto: ")
    nome_produto = input("Nome do Produto: ")
    categoria = input("Categoria: ")
    preco = float(input("Preço: "))

    
    produto = Produto(id_produto=id_produto, nome=nome_produto, categoria=categoria, preco=preco)

    
    print("\nRegistrar Interação")
    local = input("Local da interação (ex: online, loja física): ")
    horario = input("Horário da interação (ex: manhã, tarde, noite): ")
    contexto = {'local': local, 'horario': horario}
    cliente.registrar_interacao(produto, contexto)

    
    print("\nAtualizar Preferências")
    preferencias = {}
    while True:
        preferencia = input("Digite uma preferência (ou 'sair' para finalizar): ")
        if preferencia.lower() == 'sair':
            break
        nivel_preferencia = int(input(f"Nível de preferência por '{preferencia}' (1 a 10): "))
        preferencias[preferencia] = nivel_preferencia
    cliente.atualizar_preferencias(preferencias)

    
    print("\nInformações do Cliente:")
    print(cliente)
    print("\nInformações do Produto:")
    print(produto)
    print("\nInterações Registradas:")
    for interacao in cliente.interacoes:
        print(f"Produto: {interacao['produto'].nome}, Contexto: {interacao['contexto']}, Timestamp: {interacao['timestamp']}")
    print("\nPreferências Atualizadas:")
    print(cliente.preferencias)

if __name__ == "__main__":
    main()
