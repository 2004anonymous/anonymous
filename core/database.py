from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# database_url = "mysql+pymysql://root@localhost:3306/test"
database_url = "postgresql://anonymous:V7p0qCcLybCGWED8VZVECAj6oJoAhHQL@dpg-cmd4ug821fec73d0a3mg-a.oregon-postgres.render.com/admin_db_ckfr"

engine = create_engine(database_url)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
print("Connected to database !")
Base = declarative_base()

def get_db():
    try:
        return session()
    except Exception as error:
        return {"Error" : "Connection failed !"}