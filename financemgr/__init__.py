import logging 


logger = logging.getLogger(__name__)

log_handler = logging.FileHandler('app.log')
log_fmt = logging.Formatter("%(name)s - %(levelname)s - %(message)s")

log_handler.setFormatter(log_fmt)

logger.addHandler(log_handler)



from financemgr.db import * 
from financemgr.model import * 
