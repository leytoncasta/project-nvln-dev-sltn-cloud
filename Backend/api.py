from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Annotated
import Backend.models as models
from Backend.databse import SessionLocal, engine
import sqlalchemy
from sqlalchemy.orm import Session

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
    fecha_creacion: str
    fecha_tentativa_finalizacion: str
    estado: str
    id_usuario: int
    id_categoria: int

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


