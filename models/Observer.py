from abc import ABC, abstractmethod
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.Livro import Livro

class IObserver(ABC):
    
    @abstractmethod
    def atualizar(self, livro: 'Livro') -> None:
        pass

class LogLeitura(IObserver):
    def atualizar(self, livro: 'Livro') -> None:
        hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        mensagem = f"[LOG - {hora_atual}] O livro '{livro.titulo}' foi marcado como LIDO."
    
        print(mensagem)
        
        with open("historico_leitura.txt", "a", encoding='utf-8') as arquivo:
            arquivo.write(mensagem + "\n")