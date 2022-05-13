# log to console and file
import logging
import os
import sys
from logging.handlers import TimedRotatingFileHandler


def init_logger(log_dir="logs"):
    logger = logging.getLogger()
    formatter = logging.Formatter(
        "%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s")
    logger.setLevel(logging.NOTSET)

    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(formatter)
    console.setLevel(logging.INFO)
    logger.addHandler(console)

    # log to file by rotating daily
    if os.path.exists(log_dir) and os.path.isdir(log_dir):
        log_file = f"{log_dir}/now.log"
        file = TimedRotatingFileHandler(log_file, when="D", backupCount=3, encoding='utf-8')
        file.setFormatter(formatter)
        file.setLevel(logging.DEBUG)
        file.doRollover()
        logger.addHandler(file)
    logging.warning("warning")


if __name__ == '__main__':
    init_logger("logs")
