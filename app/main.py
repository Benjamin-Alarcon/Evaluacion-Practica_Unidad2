from insert import crear_libro, crear_usuario, crear_prestamo
from consultar import (listar_usuarios,listar_libros,listar_prestamos,buscar_usuario,buscar_libro,)
from actualizar import actualizar_libro, actualizar_usuario, actualizar_prestamo
from delete import eliminar_usuario, eliminar_libro, eliminar_prestamo

menu = """
1. Crear usuario
2. Crear libro
3. Crear prestamo
4. Ver usuarios
5. Ver libros
6. Ver prestamos
7. Buscar usuario por ID
8. Buscar libro por ID
9. Actualizar usuario
10. Actualizar libro
11. Actualizar prestamo
12. Eliminar usuario
13. Eliminar libro
14. Eliminar prestamo
0. Salir
"""

while True:
    print(menu)
    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        crear_usuario(nombre, correo)

    elif opcion == "2":
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        ejemplares = int(input("Ejemplares disponibles: "))
        crear_libro(titulo, autor, ejemplares)

    elif opcion == "3":
        libro_id = int(input("ID del libro: "))
        usuario_id = int(input("ID del usuario: "))
        fecha = input("Fecha: ")
        cantidad = int(input("Cantidad: "))
        crear_prestamo(libro_id, usuario_id, fecha, cantidad)

    elif opcion == "4":
        listar_usuarios()

    elif opcion == "5":
        listar_libros()

    elif opcion == "6":
        listar_prestamos()

    elif opcion == "7":
        usuario_id = int(input("ID del usuario: "))
        buscar_usuario(usuario_id)

    elif opcion == "8":
        libro_id = int(input("ID del libro: "))
        buscar_libro(libro_id)

    elif opcion == "9":
        usuario_id = int(input("ID del usuario: "))
        nombre = input("Nuevo nombre: ")
        correo = input("Nuevo correo: ")
        actualizar_usuario(usuario_id, nombre, correo)

    elif opcion == "10":
        libro_id = int(input("ID del libro: "))
        titulo = input("Nuevo titulo: ")
        autor = input("Nuevo autor: ")
        ejemplares = int(input("Nuevos ejemplares disponibles: "))
        actualizar_libro(libro_id, titulo, autor, ejemplares)

    elif opcion == "11":
        prestamo_id = int(input("ID del prestamo: "))
        estado = input("Estado (1 activo / 0 devuelto): ") == "1"
        actualizar_prestamo(prestamo_id, estado)

    elif opcion == "12":
        usuario_id = int(input("ID del usuario: "))
        eliminar_usuario(usuario_id)

    elif opcion == "13":
        libro_id = int(input("ID del libro: "))
        eliminar_libro(libro_id)

    elif opcion == "14":
        prestamo_id = int(input("ID del prestamo: "))
        eliminar_prestamo(prestamo_id)

    elif opcion == "0":
        print("Hasta luego")
        break

    else:
        print("Opcion invalida")
