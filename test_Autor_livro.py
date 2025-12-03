from models.Autor import Autor
from models.Genero  import Genero
from models.LivroEstudo import LivroEstudo
from models.FactoryLivro import FactoryLivro

a1 = Autor('Tolkien')

l1 = FactoryLivro.adicionar_livro('lazer','Senhor Dos Aneis 1',a1,Genero.AVENTURA.name)
l2 = FactoryLivro.adicionar_livro('lazer','Senhor Dos Aneis 2',a1,Genero.AVENTURA.name)
l3 = FactoryLivro.adicionar_livro('lazer','Senhor Dos Aneis 3',a1,Genero.AVENTURA.name)



a1.listar_livros()
