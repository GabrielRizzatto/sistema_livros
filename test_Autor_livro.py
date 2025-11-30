from models.Autor import Autor
from models.Genero  import Genero
from models.LivroEstudo import LivroEstudo

a1 = Autor('Roger')
l1 = LivroEstudo('Fisica',a1, Genero.NAO_FICCAO.name, 'movimento')



l1.mostrar_informações()

