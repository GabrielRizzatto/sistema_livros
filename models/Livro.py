
class Livro():
    def __init__(self,titulo:str,autor):
        self.titulo = titulo
        self.autor = autor

        autor.adicionar_livro(self.titulo)

    def __str__(self):
        return f'{self.titulo} por {self.autor.nome}'

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo:str):
        titulo = titulo.lower().title() 
        self._titulo = titulo 