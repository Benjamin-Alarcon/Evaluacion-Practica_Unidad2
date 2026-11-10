from conexion import Session
from modelos import Libro, Usuario, Prestamo


def eliminar_usuario(usuario_id):
    session = Session()
    usuario = session.get(Usuario, usuario_id)
    if usuario:
        session.delete(usuario)
        session.commit()
        print("Usuario eliminado")
    else:
        print("Usuario no encontrado")
    session.close()


def eliminar_libro(libro_id):
    session = Session()
    libro = session.get(Libro, libro_id)
    if libro:
        session.delete(libro)
        session.commit()
        print("Libro eliminado")
    else:
        print("Libro no encontrado")
    session.close()


def eliminar_prestamo(prestamo_id):
    session = Session()
    prestamo = session.get(Prestamo, prestamo_id)
    if prestamo:
        session.delete(prestamo)
        session.commit()
        print("Prestamo eliminado")
    else:
        print("Prestamo no encontrado")
    session.close()
