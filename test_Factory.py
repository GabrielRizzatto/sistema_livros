from models.FactoryLivro import FactoryLivro
from models.Autor import Autor
from models.Genero import Genero

a1 = Autor('Tolkien')

l1 = FactoryLivro.adicionar_livro('lazer','Senhor Dos Aneis 1',a1,Genero.AVENTURA.name)
l2 = FactoryLivro.adicionar_livro('lazer','Senhor Dos Aneis 2',a1,Genero.AVENTURA.name)
l3 = FactoryLivro.adicionar_livro('lazer','Senhor Dos Aneis 3',a1,Genero.AVENTURA.name)



a2 = Autor('Carl Sagan')
livro = FactoryLivro.adicionar_livro('estudo', 'Cosmos', a2, Genero.NAO_FICCAO.name, 'Astronomia')

l1.mostrar_informações()

print('')
livro.mostrar_informações()