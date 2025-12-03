from typing import TYPE_CHECKING
from abc import ABC,abstractmethod

if TYPE_CHECKING:
    from models.Autor import Autor
    from models.Genero import Genero
    from models.Observer import IObserver


class Livro(ABC):
    def __init__(self,titulo:str,autor:'Autor', genero:'Genero'):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.status = False
        self._observer: list['IObserver'] = []

        autor.adicionar_livro(self)


    def adicionar_observer(self, observador: 'IObserver') -> None:
        self._observer.append(observador)

    def notificar_observer(self) -> None:
        for observador in self._observer:
            observador.atualizar(self)


    def terminiar_leitura(self) ->None:
        self.status = True
        print(f'{self.titulo} Finalizado')
    
    @abstractmethod
    def mostrar_informações(self) -> None:
        """
        Mostra Informações do Tipo Livro
        """
        pass

    @abstractmethod
    def ler(self):
        pass

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo:str):
        titulo = titulo.lower().title() 
        self._titulo = titulo 

    
