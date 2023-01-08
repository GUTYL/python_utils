from unittest import TestCase
from python_utils.logs import init_logger
import logging


class Test(TestCase):
    def test_init_logger(self):
        init_logger()
        logging.debug("debug")
        logging.info("info")
        logging.warning("warning")
        logging.error("error")




