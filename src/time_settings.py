import datetime

ALLOWED_TIME = {
    "Monday": ("19:30", "22:00"),
    "Tuesday": ("19:30", "22:00"),
    "Wednesday": ("19:30", "22:00"),
    "Tuesday": ("19:30", "22:00"),
    "Friday": ("14:30", "00:00"),
    "Saturday": 180,
    "Sunday": 180
}

def __timestring_to_todaytime(now, timestring):
    time_array = [int(num) for num in timestring.split(":")] # [hours, minutes]
    return now.replace(hour=time_array[0], minute=time_array[1])

def __is_time_within_span(now, timespan):
    if type(timespan)==tuple:
        #print(f"Is {now.time()} within {timespan}?")
        lower_bound = __timestring_to_todaytime(now,list(timespan)[0])
        upper_bound = __timestring_to_todaytime(now,list(timespan)[1])
        if now < lower_bound or now > upper_bound:
            return False 
    return True

def is_program_locked():
    now = datetime.datetime.now()
    week_policy = list(ALLOWED_TIME.values())
    today_policy = week_policy[now.weekday()]
    return not __is_time_within_span(now, today_policy)
