from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List, Annotated
from datetime import datetime
#from Backend.models import models
#from .databse import SessionLocal, engine
import sqlalchemy
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base

 # -------------------------------------------------------------------------
URL_DATABASE = 'postgresql://adminuser:mypassword@localhost:5432/to_do_list'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
 # -------------------------------------------------------------------------
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
    fecha_creacion = Column(Date, nullable=False, index=True)
    fecha_tentativa_finalizacion = Column(Date, nullable=False, index=True)
    estado = Column(String, nullable=False, index=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    id_categoria = Column(Integer, ForeignKey('categoria.id'))
 # -------------------------------------------------------------------------
app = FastAPI()
# models.Base.metadata.create_all(bind=engine)
class Usuario(BaseModel):
    user_name: str
    last_name: str
    email: str
    contrasenia: str
    imagen_perfil: str
class Categoria(BaseModel):
    nombre: str
    descripcion: str
class Tarea(BaseModel):
    texto_tarea: str
    fecha_creacion: datetime
    fecha_tentativa_finalizacion: datetime
    estado: str
    id_usuario: int
    id_categoria: int
class IniciarSesion(BaseModel):
    email: str
    contrasenia: str
class ActualizarTarea(BaseModel):
    texto_tarea: str
    estado: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/usuarios')
async def create_usuario(usuario: Usuario, db: Session = Depends(get_db)):
    try:
        db_usuario = models.Usuario(
            user_name=usuario.user_name,
            last_name=usuario.last_name,
            email=usuario.email,
            contrasenia=usuario.contrasenia,
            imagen_perfil=usuario.imagen_perfil
        )
        db.add(db_usuario)
        db.commit()
        db.refresh(db_usuario)
        return db_usuario
    except sqlalchemy.exc.OperationalError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database connection error"
        ) from e

@app.post('/usuarios/iniciar-sesion')
async def iniciar_sesion(credentials: IniciarSesion, db: Session = Depends(get_db)):
    try:
        db_usuario = db.query(models.Usuario).filter(models.Usuario.email == credentials.email).first()
        if db_usuario is None or db_usuario.contrasenia != credentials.contrasenia:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )
        return {"message": "Login successful", "usuario": db_usuario}
    except sqlalchemy.exc.OperationalError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database connection error"
        ) from e
    
@app.post('/usuarios/iniciar-sesion')
async def iniciar_sesion(credentials: IniciarSesion, db: Session = Depends(get_db)):
    try:
        db_usuario = db.query(models.Usuario).filter(models.Usuario.email == credentials.email).first()
        if db_usuario is None or db_usuario.contrasenia != credentials.contrasenia:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )
        return {"message": "Login successful", "usuario": db_usuario}
    except sqlalchemy.exc.OperationalError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database connection error"
        ) from e

@app.post('/categorias')
async def create_categoria(categoria: Categoria, db: Session = Depends(get_db)):
    try:
        db_categoria = models.Categoria(
            nombre=categoria.nombre,
            descripcion=categoria.descripcion
        )
        db.add(db_categoria)
        db.commit()
        db.refresh(db_categoria)
        return db_categoria
    except sqlalchemy.exc.OperationalError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database connection error"
        ) from e

@app.post('/tareas')
async def create_tarea(tarea: Tarea, db: Session = Depends(get_db)):
    try:
        db_tarea = models.Tarea(
            texto_tarea=tarea.texto_tarea,
            fecha_creacion=tarea.fecha_creacion,
            fecha_tentativa_finalizacion=tarea.fecha_tentativa_finalizacion,
            estado=tarea.estado,
            id_usuario=tarea.id_usuario,
            id_categoria=tarea.id_categoria
        )
        db.add(db_tarea)
        db.commit()
        db.refresh(db_tarea)
        return db_tarea
    except sqlalchemy.exc.OperationalError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database connection error"
        ) from e

@app.put('/tareas/{id}')
async def actualizar_tarea(id: int, tarea: ActualizarTarea, db: Session = Depends(get_db)):
    try:
        db_tarea = db.query(models.Tarea).filter(models.Tarea.id == id).first()
        if db_tarea is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tarea not found"
            )

        db_tarea.texto_tarea = tarea.texto_tarea
        db_tarea.estado = tarea.estado
        db.commit()
        db.refresh(db_tarea)
        return db_tarea
    except sqlalchemy.exc.OperationalError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database connection error"
        ) from e

@app.get('/usuarios/{id}/tareas', response_model=List[Tarea])
async def obtener_tareas_por_usuario(id: int, db: Session = Depends(get_db)):
    try:
        db_tareas = db.query(models.Tarea).filter(models.Tarea.id_usuario == id).all()
        if not db_tareas:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No tasks found for this user"
            )
        return db_tareas
    except sqlalchemy.exc.OperationalError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database connection error"
        ) from e

@app.delete('/tareas/{id}')
async def eliminar_tarea(id: int, db: Session = Depends(get_db)):
    try:
        db_tarea = db.query(models.Tarea).filter(models.Tarea.id == id).first()
        if db_tarea is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tarea not found"
            )

        db.delete(db_tarea)
        db.commit()
        return {"message": "Tarea deleted successfully"}
    except sqlalchemy.exc.OperationalError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database connection error"
        ) from e
    
@app.get('/tareas/{id}', response_model=Tarea)
async def obtener_tarea_por_id(id: int, db: Session = Depends(get_db)):
    try:
        db_tarea = db.query(models.Tarea).filter(models.Tarea.id == id).first()
        if db_tarea is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tarea not found"
            )
        return db_tarea
    except sqlalchemy.exc.OperationalError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database connection error"
        ) from e

@app.delete('/categorias/{id}')
async def eliminar_categoria(id: int, db: Session = Depends(get_db)):
    try:
        db_categoria = db.query(models.Categoria).filter(models.Categoria.id == id).first()
        if db_categoria is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Categoria not found"
            )

        db.delete(db_categoria)
        db.commit()
        return {"message": "Categoria deleted successfully"}
    except sqlalchemy.exc.OperationalError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database connection error"
        ) from e

@app.get('/categorias', response_model=List[Categoria])
async def obtener_lista_de_categorias(db: Session = Depends(get_db)):
    try:
        db_categorias = db.query(models.Categoria).all()
        if not db_categorias:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No categories found"
            )
        return db_categorias
    except sqlalchemy.exc.OperationalError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database connection error"
        ) from e
    