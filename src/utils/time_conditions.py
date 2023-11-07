import datetime
import logging

PROGRAM_UPTIME={}

def is_program_locked(allowed_time:dict, max_allowed_minutes:dict, check_interval_minutes:int):
    """Checks whether the program should be locked right now.
    Returns true if the program should be currently locked. Returns false otherwise.

    Parameters:
    - allowed_time [dict]: the allowed time configuration per weekday
    - max_allowed_minutes [dict]: the max allowed minutes configuration per weekday
    - check_interval_minutes [int]: how often is the program status checked
    """
    now = datetime.datetime.now()
    if now.date() not in PROGRAM_UPTIME.keys():
        PROGRAM_UPTIME[now.date()]=0
    today_uptime=PROGRAM_UPTIME[now.date()] # lower bound estimation of todays uptime
    logging.info(f"Estimated uptime for today: {today_uptime}")
    PROGRAM_UPTIME[now.date()] = PROGRAM_UPTIME[now.date()] + check_interval_minutes # update uptime for next check
    today_policy_clock = __get_today_policy(now, allowed_time)
    today_policy_span = __get_today_policy(now, max_allowed_minutes)
    is_allowed = __is_time_within_span(now, today_policy_clock) and __is_timespan_ok(today_uptime, today_policy_span)
    return not is_allowed


def __get_today_policy(now, week_policy):
    week_policy_list = list(week_policy.values())
    return week_policy_list[now.weekday()]

def __timestring_to_todaytime(now, timestring):
    """Converts a timestring to the related datetime of today.
    
    Parameters: 
    - now [datetime] 
    - timestring [str]: Expects a format like "22:15" (hh:mm) for the timestring.
    """
    time_array = [int(num) for num in timestring.split(":")] # [hours, minutes]
    return now.replace(hour=time_array[0], minute=time_array[1])

def __is_timespan_ok(uptime_minutes, allowed_uptime_minutes):
    return uptime_minutes < allowed_uptime_minutes

def __is_time_within_span(now, timespan):
    if type(timespan)==tuple:
        logging.debug(f"Is {now.time()} within allowed timespan {timespan}?")
        lower_bound = __timestring_to_todaytime(now,list(timespan)[0])
        upper_bound = __timestring_to_todaytime(now,list(timespan)[1])
        if now < lower_bound or now > upper_bound:
            return False 
    return True
