from sys import stdin
from UserDAO import UserDAO, User

if __name__ == "__main__":
    ans = 1
    while ans:
        print("Seleccione la opción que requiera:")
        print("1 Listar usuarios")
        print("2 Agregar usuario")
        print("3 Actualizar usuario")
        print("4 Eliminar usuario")
        print("5 Salir")
        option = int(input())

        if option == 1:
            for r in UserDAO.select():
                print(r)

        elif option == 2:
            name, passw = None, None
            print("Escribe el nombre de usuario: ")
            name = stdin.readline().strip()
            print("Escribe la contraseña: ")
            passw = stdin.readline().strip()
            u1 = User(username = name, password = passw)
            print(UserDAO.insert(u1))

        elif option == 3:
            print("Escribe el id del usuario a actualizar: ")
            id = int(input())
            name, passw = None, None
            print("Escribe el nuevo nombre de usuario: ")
            name = stdin.readline().strip()
            print("Escribe la nueva contraseña: ")
            passw = stdin.readline().strip()
            u1 = User(username = name, password = passw)
            UserDAO.update(id, u1)

        elif option == 4:
            print("Escribe el id a eliminar: ")
            id = int(input())
            UserDAO.delete(id)
            
        else:
            ans = 0
