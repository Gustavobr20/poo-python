from interfaces import DatabaseInterface

class MySQLDB(DatabaseInterface):

    def __init__(self) -> None:
        self.__conexao = 'Mysql'

    def conectar(self) -> str:
        print('Conectando ao banco de dados MySQL...')
        return self.__conexao
    
    def desconectar(self) -> str:
        print('Desconectando do banco MySQL...')