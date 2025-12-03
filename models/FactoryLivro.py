from models.LivroEstudo import LivroEstudo
from models.LivroLarzer import LivroLazer

class FactoryLivro():
    @staticmethod
    def adicionar_livro(tipo:str, *args) -> LivroEstudo|LivroLazer:
        """
        Ordem: tipo, titulo, autor, genero, conteudo: caso tipo = estudo
        """
        if tipo == 'lazer':
            titul, auto, gener = args
            return LivroLazer(titul, auto, gener)
        
        if tipo == 'estudo':
            titulo, autor, genero, conteudo = args
            return LivroEstudo(titulo, autor, genero, conteudo)


