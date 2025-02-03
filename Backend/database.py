from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'postgresql://adminuser:mypassword@localhost:5432/to_do_list'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()