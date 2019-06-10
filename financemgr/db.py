from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from financemgr.config import DB_URL 

from financemgr import logger  

Base = declarative_base()

logger.debug("Initialize engine with url at: {}".format(DB_URL))
engine = create_engine(DB_URL)

Session = sessionmaker()
Session.configure(bind = engine)




