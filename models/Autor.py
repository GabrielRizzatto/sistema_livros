from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.Livro import Livro

class Autor():
    def __init__(self, nome:str):
        self.nome = nome
        self.livros = []


    def adicionar_livro(self, livro:'Livro') -> None:
        """ 
        Adiciona Livros.
        """
        self.livros.append(livro.titulo)

    def listar_livros(self) -> None:
        """
        Lista os Livros do autor. Caso não tenha Livros retorna uma mensagem.
        """
        if not self.livros:
            print(f'Nenhum Livro de {self.nome} cadastrado')
        else:
            print(f'Obras de {self.nome}')
            for livro in self.livros:
                print(f'- {livro}')

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome:str):
        nome = nome.lower().title() 
        self._nome = nome


    

    

