from models.Autor import Autor
from models.Genero import Genero
from models.FactoryLivro import FactoryLivro
from models.Observer import LogLeitura  


autor = Autor('Carl Sagan')
livro = FactoryLivro.adicionar_livro('estudo', 'Cosmos', autor, Genero.NAO_FICCAO.name, 'Astronomia')


autor2 = Autor('Platão')

livro2 = FactoryLivro.adicionar_livro('lazer','A Republica', autor2, Genero.FILOSOFIA.name, )

sistema_log = LogLeitura()
livro.adicionar_observer(sistema_log)



livro2.adicionar_observer(sistema_log)


livro.ler()
livro2.ler()