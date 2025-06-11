from datetime import datetime
import os

import logging
from logging.handlers import RotatingFileHandler


def get_log_path():
    """
    Generate a new log file path with a timestamp.

    Returns:
        str: A unique log file name in the format 'app_log-YYYY-MM-DD-HH-MM-SS.log'.
    """
    return os.path.join("logs", f"app_log{datetime.now().strftime('-%Y-%m-%d-%H-%M-%S')}.log")

LOG_PATH = get_log_path()

# Creates a dir if the folder is not found.
os.makedirs("logs", exist_ok=True)

def get_logger(name: str = "automation-bot") -> logging.Logger:
    """
    Returns a logger that logs to both console and file.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        file_handler = RotatingFileHandler(LOG_PATH, maxBytes=1_000_000, backupCount=3)
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(asctime)s — %(levelname)s — %(name)s — %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
