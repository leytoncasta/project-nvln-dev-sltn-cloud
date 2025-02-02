from sqlalchemy import Column, Integer, String, ForeignKey
from  Backend.databse import Base 

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, nullable=False, index=True)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, index=True)
    contrasenia = Column(String, nullable=False)
    imagen_perfil = Column(String, nullable=False)

class Categoria(Base):
    __tablename__ = 'categoria'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False, index=True)
    descripcion = Column(String, nullable=False, index=True)

class Tarea(Base):
    __tablename__ = 'tarea'
    id = Column(Integer, primary_key=True, index=True)
    texto_tarea = Column(String, nullable=False, index=True)
    fecha_creacion = Column(String, nullable=False, index=True)
    fecha_tentativa_finalizacion = Column(String, nullable=False, index=True)
    estado = Column(String, nullable=False, index=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    id_categoria = Column(Integer, ForeignKey('categoria.id'))