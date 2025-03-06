class Cliente:  # Nome da classe corrigido para "Cliente"
    def __init__(self, id_cliente, nome, idade, genero):
        self.id_cliente = id_cliente
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.perfil = {}
        self.interacoes = []
        self.preferencias = {}

    def estabelecer_perfil(self, interesses):
        
        self.perfil = interesses

    def registrar_interacao(self, produto, contexto):
        
        interacao = {
            'produto': produto,
            'contexto': contexto,
            'timestamp': self._get_timestamp()
        }
        self.interacoes.append(interacao)

    def capturar_contexto(self, contexto):
        
        self.contexto_atual = contexto

    def atualizar_preferencias(self, preferencias):
        
        self.preferencias.update(preferencias)

    def _get_timestamp(self):
        
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"Cliente(ID: {self.id_cliente}, Nome: {self.nome}, Idade: {self.idade}, Gênero: {self.genero})"