from conexion import Session
from modelos import Libro, Usuario, Prestamo


def listar_usuarios():
    session = Session()
    usuarios = session.query(Usuario).all()
    for usuario in usuarios:
        print(f"ID: {usuario.id}, Nombre: {usuario.nombre}, Correo: {usuario.correo}")
    session.close()


def listar_libros():
    session = Session()
    libros = session.query(Libro).all()
    for libro in libros:
        print(f"ID: {libro.id}, Titulo: {libro.titulo}, Autor: {libro.autor}, Disponibles: {libro.ejemplares_disponibles}")
    session.close()


def listar_prestamos():
    session = Session()
    prestamos = session.query(Prestamo).all()
    for prestamo in prestamos:
        print(f"ID: {prestamo.id}, Libro: {prestamo.libro_id}, Usuario: {prestamo.usuario_id}, Fecha: {prestamo.fecha}, Cantidad: {prestamo.cantidad},Estado: {prestamo.estado}")
    session.close()


def buscar_usuario(usuario_id):
    session = Session()
    usuario = session.get(Usuario, usuario_id)
    if usuario:
        print(f"ID: {usuario.id}, Nombre: {usuario.nombre}, Correo: {usuario.correo}")
    else:
        print("Usuario no encontrado")
    session.close()


def buscar_libro(libro_id):
    session = Session()
    libro = session.get(Libro, libro_id)
    if libro:
        print(f"ID: {libro.id}, Titulo: {libro.titulo}, Autor: {libro.autor}, Disponible: {libro.ejemplares_disponibles}")
    else:
        print("Libro no encontrado")
    session.close()
