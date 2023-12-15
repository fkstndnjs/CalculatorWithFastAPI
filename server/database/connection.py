from sqlmodel import SQLModel, Session, create_engine
from models.exrpession import Expression

filename = "mem.db"
dialect = "sqlite"
db_conn_url = f"{dialect}:///{filename}"
c_args = {"check_same_thread": False}

engine = create_engine(db_conn_url, echo=True, connect_args=c_args)

def conn():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
