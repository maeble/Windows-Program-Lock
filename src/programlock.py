import utils.close_program_loop as cpl
import logging
import os
from settings import *

APP_DATA_DIR=os.getenv('LOCALAPPDATA') # the log file is created in a subdirectory of LOCALAPPDATA
print("Log files are written to a subdirectory of", APP_DATA_DIR)
logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', filename=f'{APP_DATA_DIR}\{LOG_FILE_NAME}', encoding='utf-8', level=LOG_LEVEL)
try:
    cpl.close_program_loop(PROGRAM, LOCK_POLICY, sleep_minutes=CHECK_INTERVAL_MINUTES)
except Exception as error:
    logging.error(f"ProgramLock crashed: {error}")
