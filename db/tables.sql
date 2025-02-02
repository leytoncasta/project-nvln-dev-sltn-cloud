CREATE TABLE usuario (
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    contrasenia VARCHAR(255) NOT NULL,
    imagen_perfil VARCHAR(255)
);

CREATE TABLE categoria (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion VARCHAR(255) NOT NULL
);

CREATE TABLE tarea (
    id SERIAL PRIMARY KEY,
    texto_tarea VARCHAR(255) NOT NULL,
    fecha_creacion DATE NOT NULL,
    fecha_tentativa_finalizacion DATE,
    estado VARCHAR(50),
    id_usuario INT REFERENCES usuario(id),
    id_categoria INT REFERENCES categoria(id)
);
