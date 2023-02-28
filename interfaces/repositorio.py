from abc import ABC, abstractmethod

class RepositorioInterface(ABC):
    
    @abstractmethod
    def select(self, db_connection: any) -> None:
        pass

    @abstractmethod
    def insert(self, db_connection: any) -> None:
        pass
