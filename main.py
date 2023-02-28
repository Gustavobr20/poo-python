from repository import Repositorio
from databases import MySQLDB, PostgresDB

db_conn = MySQLDB()
repo = Repositorio()

repo.insert(db_conn)
repo.select(db_conn)