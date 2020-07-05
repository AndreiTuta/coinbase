import os 

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

def generate_name(current):
    date_str  = str(current).replace(" ", "")
    file_name = date_str[:(len(date_str) -15)]
    return 'result'+file_name+'.csv'
    
# needs redoing
# def handle_arg(x):
#     timer = 0
#     write_hits = 0
#     write_groups = 0
#     mode = modes[0]
#     if (isinstance(x, str)):
#         if(x in modes):
#             print('Mode set to ' + x)
#             mode = x
#         else:
#              if (isinstance(parse_string_to_int(x), int)):
#                 if(timer == 0):
#                     print('Time set to ' + x)
#                     timer = x
#                 else:
#                     if(write_hits == 0):
#                         print('Write Hits set to ' + x)
#                         write_hits = x
#                     else:
#                         if(write_groups == 0):
#                             print('Write groups set to ' + x)
#                             write_groups = x
#              else:
#                 print('Undefined ' + x)
#     return [timer, mode, write_hits, write_groups]

def write_results(path, sample, current):
    filepath = 'results/' + generate_name(current)
    print(filepath)
    if os.path.exists(filepath):
        append_write = 'a' # append if already exists
    else:
        append_write = 'w' # make a new file if not

    print(append_write)
    fo = open(filepath, append_write)
    index = 0
    for response in sample:
        fo.write(response)
        index +=1
    fo.close