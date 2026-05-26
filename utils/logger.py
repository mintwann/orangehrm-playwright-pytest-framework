import os
import logging
from datetime import datetime
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
LOGS_DIR = ROOT_DIR / "logs"

# Ensure log directory exists dynamically
os.makedirs(LOGS_DIR, exist_ok=True)

log_file_name = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
log_file_path = LOGS_DIR / log_file_name

# Initialize custom logger
logger = logging.getLogger("OrangeHRM-Framework")
logger.setLevel(logging.DEBUG)

# Prevent duplicate handlers if logger is initialized multiple times
if not logger.handlers:
    formatter = logging.Formatter(
        fmt="[%(asctime)s] [%(levelname)s] %(filename)s:%(lineno)d - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # File Handler (Only write log to file, Pytest will handle console logs natively)
    file_handler = logging.FileHandler(log_file_path, encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)