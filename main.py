from python_utils.logs import init_logger
import logging
import time
init_logger()
for i in range(10):
    time.sleep(60)
    logging.debug("debug")
    logging.info("info")
    logging.warning("warning")
    logging.error("error")