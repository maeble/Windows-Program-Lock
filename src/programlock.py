import close_program_loop as main
import logging
import os

# CONFIGURATION ###################################################################

PROGRAM="steam.exe" # the program that is to be locked
LOG_LEVEL=logging.ERROR
CHECK_INTERVAL_MINUTES=5 

###################################################################################

APP_DATA_DIR=os.getenv('LOCALAPPDATA') # the log file is created in a subdirectory of LOCALAPPDATA
print("Log files are written to a subdirectory of", APP_DATA_DIR)
logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', filename=f'{APP_DATA_DIR}\programlock.log', encoding='utf-8', level=LOG_LEVEL)
try:
    main.close_program_loop(PROGRAM, sleep_minutes=CHECK_INTERVAL_MINUTES)
except Exception as error:
    logging.error(f"ProgramLock crashed: {error}")