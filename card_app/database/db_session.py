# sqlalchemy
import sqlalchemy as sa

# sql-orm - session
from sqlalchemy.orm import sessionmaker

# libs
from pathlib import Path

# sql-orm
from sqlalchemy.orm import Session
from sqlalchemy.future.engine import Engine

# models
from card_app.models.model_base import ModelBase

__engine = None

print('--DB in execution or reload--')

def create_engine(sqlite: bool = True):
    global __engine
    
    if __engine:
        return
    
    if sqlite:
        arquivo_db = 'db/cardapp.sqlite'
        folder = Path(arquivo_db).parent
        folder.mkdir(parents=True, exist_ok=True)
        
        conn_str = f'sqlite:///{arquivo_db}'
        __engine = sa.create_engine(url=conn_str, echo=False, connect_args={"check_same_thread": False})
    
    return __engine
        
def create_session():
    global __engine
    
    if not __engine:
        create_engine(sqlite=True) 
        
    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)
    session: Session = __session()
    
    return session

def create_tables():
    global __engine 
    
    if not __engine:
        create_engine(sqlite=True)
        
    import card_app.models.__all_models
    ModelBase.metadata.drop_all(__engine)
    ModelBase.metadata.create_all(__engine)
    
