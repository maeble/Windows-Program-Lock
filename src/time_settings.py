import datetime
import logging

# CONFIGURATION ###################################################################

ALLOWED_TIME = {
    "Monday": ("19:30", "22:15"),
    "Tuesday": ("19:30", "22:15"),
    "Wednesday": ("19:30", "22:15"),
    "Tuesday": ("19:30", "22:15"),
    "Friday": ("14:30", "23:59"),
    "Saturday": 180,
    "Sunday": 180
}

###################################################################################

def is_program_locked(allowed_time:dict=ALLOWED_TIME):
    """Checks whether the program should be locked right now.
    Returns true if the program should be currently locked. Returns false otherwise.

    Parameters:
    - allowed_time [dict]: the allowed time configuration per weekday
    """
    now = datetime.datetime.now()
    week_policy = list(allowed_time.values())
    today_policy = week_policy[now.weekday()]
    return not __is_time_within_span(now, today_policy)

def __timestring_to_todaytime(now, timestring):
    """Converts a timestring to the related datetime of today.
    
    Parameters: 
    - now [datetime] 
    - timestring [str]: Expects a format like "22:15" (hh:mm) for the timestring.
    """
    time_array = [int(num) for num in timestring.split(":")] # [hours, minutes]
    return now.replace(hour=time_array[0], minute=time_array[1])

def __is_time_within_span(now, timespan):
    if type(timespan)==tuple:
        logging.debug(f"Is {now.time()} within allowed timespan {timespan}?")
        lower_bound = __timestring_to_todaytime(now,list(timespan)[0])
        upper_bound = __timestring_to_todaytime(now,list(timespan)[1])
        if now < lower_bound or now > upper_bound:
            return False 
    return True
