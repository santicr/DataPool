from Cursor import Cursor
from User import User
from Logger_base import log

class UserDAO:
    _SELECT = "SELECT * FROM public.user"
    _INSERT = "INSERT INTO public.user(username, password) VALUES(%s, %s)"
    _UPDATE = "UPDATE public.user SET username = %s, password = %s WHERE id_user = %s"
    _DELETE = "DELETE FROM public.user WHERE id_user = %s"

    @classmethod
    def select(cls):
        with Cursor() as cursor:
            cursor.execute(cls._SELECT)
            return cursor.fetchall()
    
    @classmethod
    def insert(cls, user):
        with Cursor() as cursor:
            values = (user.username, user.password)
            cursor.execute(cls._INSERT, values)
            log.debug(f"Usuario ingresado correctamente")
            return cursor.rowcount
    
    @classmethod
    def update(cls, id, new_user):
        with Cursor() as cursor:
            values = (new_user.username, new_user.password, id)
            cursor.execute(cls._UPDATE, values)
            log.debug(f"Usuario actualizado correctamente {id}")
            return cursor.rowcount
    
    @classmethod
    def delete(cls, id):
        with Cursor() as cursor:
            cursor.execute(cls._DELETE, (id,))
            log.debug(f"Usuario eliminado correctamente {id}")
