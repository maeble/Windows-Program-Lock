import logging

# Required configuration
#######################################################################################################

# the program that is to be locked
PROGRAM="steam.exe" 

# the LOCK_POLICY defines, when and how long the program is allowed to run.
# only when both configurations say that the program is allowed to run, the program can be used.
# note: this is an example configuration. please adapt it to your needs.
# please do not delete any lines.
LOCK_POLICY = {

    # define when the program is allowed to run.
    "ALLOWED_TIME": {
        "Monday": ("00:00", "00:00"), # the program use is not allowed on Monday    
        "Tuesday": ("19:30", "22:15"), # allowed from 19:30 -to 22:15
        "Wednesday": ("19:30", "22:15"), 
        "Tuesday": ("19:30", "22:15"),
        "Friday": ("14:30", "23:59"),
        "Saturday": ("00:00", "23:59"), # allowed for the whole day
        "Sunday": ("00:00", "23:59"), 
    }, 

    # define how long the program is allowed to run (in minutes)
    "MAX_ALLOWED_MINUTES": {
        "Monday": 0, # the program use is not allowed on Monday
        "Tuesday": 24*60, # the program is allowed to run 24 hours
        "Wednesday": 24*60,
        "Tuesday": 24*60,
        "Friday": 24*60,
        "Saturday": 3*60, # the program is allowed to run max. 3 hours
        "Sunday": 180 # the program is allowed to run max. 3 hours
    },
}

# Advanced configuration
#######################################################################################################

CHECK_INTERVAL_MINUTES=1 # how often does the app check whether the controlled program runs unallowed
LOG_FILE_NAME="programlock.error.log" 
LOG_LEVEL=logging.ERROR 
