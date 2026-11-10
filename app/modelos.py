from sqlalchemy import String, Integer, Column, CheckConstraint, Boolean, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship

class Base(DeclarativeBase):
    pass

class Libro(Base):
    __tablename__ = 'libros'
    __table_args__ = (
        CheckConstraint("ejemplares_disponibles >= 0", name="ck_ejemplares"),
    )
    
    id= Column(Integer, nullable= False, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable= False)
    autor = Column(String, nullable = False)
    ejemplares_disponibles = Column(Integer, nullable = False)

    prestamos = relationship("Prestamo", back_populates="libros")

class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, nullable = False, primary_key= True, autoincrement=True)
    nombre = Column(String, nullable=False)
    correo = Column(String, nullable=False, unique=True)
    
    prestamos = relationship("Prestamo", back_populates="usuarios")
    
    
class Prestamo(Base):
    __tablename__ = "prestamos"
    __table_args__ = (
        CheckConstraint("cantidad > 0", name="ck_cantidad"),
    )
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    libro_id = Column(Integer, ForeignKey("libros.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    fecha = Column(String, nullable=False)
    cantidad = Column(Integer, nullable= False)
    estado = Column(Boolean, nullable=False)
    
    libros = relationship("Libro", back_populates='prestamos')
    usuarios = relationship("Usuario", back_populates='prestamos')
    
