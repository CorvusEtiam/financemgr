from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from financemgr.db import Base 

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    accounts = relationship(
            "Account", 
            backref="user", 
            cascade = "all, delete, delete-orphan", 
            single_parent = True, 
            order_by = "desc(Account.id)")    

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    records = relationship(
            "Record", 
            backref="account", 
            cascade = "all, delete, delete-orphan", 
            single_parent = True, 
            order_by = "desc(Record.id)")

class Record(Base):
    __tablename__ = "records"
    id = Column(Integer, primary_key = True)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    record_title = Column(String)
    record_value = Column(Float)
    record_timestamp = Column(DateTime, default = datetime.utcnow, onupdate  = datetime.utcnow)

