from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = f"{"sqlite"}:///{"storage.db"}"
        self.__engine = None
        
    def connect_to_db(self) -> None:
        self.__engine = create_engine(self.__connection_string)
        self.__session = None

    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_maker = sessionmaker()
        self.__session = session_maker(bind=self.__engine)
        return self
        
    def __exit__(self):
        self.__session.close()
