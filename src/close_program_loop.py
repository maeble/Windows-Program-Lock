import subprocess
import psutil
import time
import time_settings
import logging

def close_program_loop(task:str, sleep_minutes:int=5):
    """Runs an infinite loop, that checks whether the task is allowed to run
    and kills it if it is not allowed to run.

    Parameter:
    - task [str]: the task to be closed
    - sleep_minutes [int]: how often it is checked whether the program is running
    """
    while True:
        logging.info("Checking program status...")
        if __is_program_running(task) and time_settings.is_program_locked():
            logging.info("Killing program...")
            subprocess.call(f"TASKKILL /F /IM {task}", shell=True)
            logging.info("Program killed.")
        else:
            logging.info("Nothing to do here.")
        logging.info("Going to sleep...")
        time.sleep(sleep_minutes*60)

def __is_program_running(task:str):    
    return task in (p.name() for p in psutil.process_iter())
