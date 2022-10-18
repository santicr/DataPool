from Connection import Connection
from Logger_base import log

class Cursor:
    def __init__(self) -> None:
        self._cursor = None
        self._conn = None
    
    def __enter__(self):
        self._conn = Connection.getConn()
        self._cursor = self._conn.cursor()
        log.debug(f"Inicializando cursor.. {self._cursor}")
        return self._cursor
    
    def __exit__(self, e_type, e_value, e_detail):
        log.debug("Se esta cerrando el cursor...")
        if e_value:
            log.error(f"Hubo un error, se hará rollback.. {e_type} {e_value} {e_detail}")
            self._conn.rollback()
        else:
            log.debug("Se hara commit, todo correcto :)")
            self._conn.commit()

        self._cursor.close()
        Connection.freeConn(self._conn)