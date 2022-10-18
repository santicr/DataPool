from psycopg2 import pool
from Logger_base import log
import sys

class Connection:
    _USER = "postgres"
    _PASSWORD = "admin"
    _HOST = "127.0.0.1"
    _PORT = "5432"
    _DATABASE = "test_db"
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def getPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                    user = cls._USER,
                    password = cls._PASSWORD,
                    host = cls._HOST,
                    port = cls._PORT,
                    database = cls._DATABASE
                )
                log.debug("Se ha obtenido el pool de conexiones correctamente.")
            except Exception as e:
                log.error(f"Hubo un error al intentar obtener el pool: {e}")
                sys.exit()
        return cls._pool
    
    @classmethod
    def getConn(cls):
        try:
            conn = cls.getPool().getconn()
            log.debug(f"Se ha obtenido una conexión: {conn}")
            return conn
        except Exception as e:
            log.error(f"Hay un problema al obtener una conexión: {e}")
            sys.exit()

    @classmethod
    def freeConn(cls, conn):
        cls.getPool().putconn(conn)
        log.debug("Se ha devuelto correctamente la conexión al pool :)")

    @classmethod
    def closePool(cls):
        try:
            cls.getPool().closeall()
            log.debug("Se ha cerrado correctamente el pool")
        except Exception as e:
            log.error(f"No se ha podido cerrar el pool: {e}")

if __name__ == "__main__":
    c1 = Connection.getConn()
    c2 = Connection.getConn()