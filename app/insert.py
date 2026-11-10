from conexion import Session
from modelos import Libro, Usuario, Prestamo


def crear_libro(titulo, autor, ejemplares):
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
    libro = Libro(titulo=titulo, autor=autor, ejemplares_disponibles=ejemplares)
    session.add(libro)
    session.commit()
    session.close()
    print("Libro creado")


def crear_usuario(nombre, correo):
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
    existe = session.query(Usuario).filter(Usuario.correo == correo).first()
    if existe:
        print("Ese correo ya esta registrado")
        session.close()
        return

    usuario = Usuario(nombre=nombre, correo=correo)
    session.add(usuario)
    session.commit()
    session.close()
    print("Usuario creado")


def crear_prestamo(libro_id, usuario_id, fecha, cantidad):
    if fecha.strip() == "":
        print("La fecha no puede estar vacia")
        return
    if cantidad <= 0:
        print("La cantidad debe ser mayor a 0")
        return

    session = Session()
    libro = session.get(Libro, libro_id)
    usuario = session.get(Usuario, usuario_id)

    if libro is None:
        print("El libro no existe")
    elif usuario is None:
        print("El usuario no existe")
    elif libro.ejemplares_disponibles < cantidad:
        print("No hay suficientes ejemplares")
    else:
        prestamo = Prestamo(
            libro_id=libro_id,
            usuario_id=usuario_id,
            fecha=fecha,
            cantidad=cantidad,
            estado=True,
        )
        session.add(prestamo)
        libro.ejemplares_disponibles = libro.ejemplares_disponibles - cantidad
        session.commit()
        print("Prestamo creado")

    session.close()
