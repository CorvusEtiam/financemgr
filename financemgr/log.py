import logging 
import os 

from financemgr.config import LOG_PATH 

def setup_logger(name = "app"):
    formatter = logging.Formatter(fmt = "%(asctime)s : %(levelname)s : %(module)s : %(message)s")
    
    con_handler  = logging.StreamHandler()
    con_handler.setLevel(logging.DEBUG)
    con_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(os.path.join(LOG_PATH, f"{name}.log"), mode = 'a')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.addHandler(con_handler)
    logger.addHandler(file_handler)
    
    return logger 


    
    
