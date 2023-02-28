from abc import ABC, abstractmethod

class DatabaseInterface(ABC):

    @abstractmethod
    def conectar(self) -> str:
        pass
    
    @abstractmethod
    def desconectar(self) -> str:
        pass