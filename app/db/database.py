from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres@postgresserver/db"

# the engine is a factory that can create new database connections for us

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True, future=True
    )

# this is not a session yet, we are configuring the sessionsmaker that will create sessions later
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# is inherited by our ORM models 
Base = declarative_base()

