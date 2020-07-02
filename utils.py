def parse_string_to_int(string):
    try:
        string_int = int(string)
        return(string_int)
    except ValueError:
        # Handle the exception
        print('Please enter an integer ' + string)

def parse_string_to_bool(string):
    return bool(string)

def get_current_hour_minutes_seconds(current):
    if(current.minute < 10): 
        minute = '0' + str(current.minute)
    else:
        minute = str(current.minute)
    return str(current.hour) + ':' + minute + ':' + str(current.second)


def get_current_hour_minutes(current):
    if(current.minute < 10): 
        minute = '0' + str(current.minute)
    else:
        minute = str(current.minute)
    return str(current.hour) + ':' + minute
