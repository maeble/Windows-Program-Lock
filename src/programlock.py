import close_program_loop as main
import logging

# CONFIGURATION ###################################################################

PROGRAM="steam.exe" # the program that is to be locked

###################################################################################

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', filename='programlock.log', encoding='utf-8', level=logging.INFO)
try:
    main.close_program_loop(PROGRAM)
except Exception as error:
    logging.error(f"ProgramLock crashed: {error}")
