class Autor():
    def __init__(self, nome:str):
        self.nome = nome
        self.livros = []


    def adicionar_livro(self, livro:str) -> None:
        """ 
        Adiciona Livros.
        """
        self.livros.append(livro)

    def listar_livros(self) -> None:
        """
        Lista os Livros do autor. Caso não tenha Livros retorna uma mensagem.
        """
        if not self.livros:
            print(f'Nenhum Livro de {self.nome} cadastrado')
        for livro in self.livros:
            print(f'- {livro}')

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome:str):
        nome = nome.lower().title() 
        self._nome = nome


    

    

