#data base
from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine("sqlite:///finance.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Transaction(Base):
    __tablename__ = "Transactions"

    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    category = Column(String)
    date = Column(String)
    type = Column(String) # income or expense

def initialise_database():
    Base.metadata.create_all(engine)