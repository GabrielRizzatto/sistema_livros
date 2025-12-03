from models.Livro import Livro

class LivroLazer(Livro):
    def __init__(self, titulo, autor, genero):
        super().__init__(titulo, autor, genero)

    def mostrar_informações(self) ->None:
            print(f'Nome: {self.titulo}')       
            print(f'Autor: {self.autor.nome}')
            print(f'Genero: {self.genero}')
            print(f'Status : {self.status}')
    
    def ler(self) -> None:
        if self.status == True:
            print(f'{self.titulo} já foi lido')
            return None
    
        self.status = True
        self.notificar_observer()