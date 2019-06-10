import logging 

logging.basicConfig(filename = "app.log", level = logging.DEBUG)

from financemgr.db import * 
from financemgr.model import * 
from financemgr.ui import * 

from financemgr.ui import AppController

def app():
    test_app = AppController()
    test_app.run()