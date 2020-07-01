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
    return str(current.hour) + ':' + str(current.minute)+ ':' + str(current.second)


def get_current_hour_minutes(current):
    return str(current.hour) + ':' + str(current.minute)
