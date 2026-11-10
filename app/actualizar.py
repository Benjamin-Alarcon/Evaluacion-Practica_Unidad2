from conexion import Session
from modelos import Libro, Usuario, Prestamo


def actualizar_libro(libro_id, titulo, autor, ejemplares):
    if titulo.strip() == "":
        print("El titulo no puede estar vacio")
        return
    if autor.strip() == "":
        print("El autor no puede estar vacio")
        return
    if ejemplares < 0:
        print("Los ejemplares deben ser 0 o mas")
        return

    session = Session()
    libro = session.get(Libro, libro_id)
    if libro is None:
        print("Libro no encontrado")
    else:
        libro.titulo = titulo
        libro.autor = autor
        libro.ejemplares_disponibles = ejemplares
        session.commit()
        print("Libro actualizado")
    session.close()


def actualizar_usuario(usuario_id, nombre, correo):
    if nombre.strip() == "":
        print("El nombre no puede estar vacio")
        return
    if correo.strip() == "":
        print("El correo no puede estar vacio")
        return
    if "@" not in correo or "." not in correo:
        print("El correo no es valido")
        return

    session = Session()
    usuario = session.get(Usuario, usuario_id)
    if usuario is None:
        print("Usuario no encontrado")
    else:
        existe = (
            session.query(Usuario)
            .filter(Usuario.correo == correo, Usuario.id != usuario_id)
            .first()
        )
        if existe:
            print("Ese correo ya esta registrado")
        else:
            usuario.nombre = nombre
            usuario.correo = correo
            session.commit()
            print("Usuario actualizado")
    session.close()


def actualizar_prestamo(prestamo_id, estado):
    session = Session()
    prestamo = session.get(Prestamo, prestamo_id)
    libro = session.get(Libro, prestamo.libro_id)
    if prestamo is None:
        print("Prestamo no encontrado")
    if prestamo.estado == False:
        raise ValueError("El prestamo ya fue devuelto")
    else:
        if estado == False:
            libro.ejemplares_disponibles += prestamo.cantidad
            prestamo.estado = estado
            session.commit()
            print("Prestamo actualizado")
        session.close()
