from models.Livro import Livro

class LivroEstudo(Livro):
    def __init__(self, titulo, autor, genero, conteudo):
        super().__init__(titulo, autor, genero)
        self.conteudo = conteudo

    def mostrar_informações(self) ->None:
            print(f'Nome: {self.titulo}')       
            print(f'Autor: {self.autor.nome}')
            print(f'Genero: {self.genero}')
            print(f'Conteudo: {self.conteudo}')
            print(f'Status : {self.status}')


            
    def ler(self) -> None:
        if self.status == True:
            print(f'{self.titulo} já foi lido')
            return None
    
        self.status = True
        self.notificar_observer()
                  



