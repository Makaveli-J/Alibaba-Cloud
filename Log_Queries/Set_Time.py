import time


def get_time() -> tuple:
    print('Please set start time in the following format')
    print('mm/dd/yyyy or mm/dd/yyyy HH:MM:SS (00:00:00 by default)')
    from_time = str(input('Start Time: '))

    try:
        from_time = time.mktime(time.strptime(from_time, '%m/%d/%Y'))
    except:
        try:
            from_time = time.mktime(time.strptime(from_time, '%m/%d/%Y %H:%M:%S'))
        except:
            print('Invalid Time Format')
            exit()

    print('****************************')

    print('Please set end time in the following format')
    print('mm/dd/yyyy or mm/dd/yyyy HH:MM:SS (00:00:00 by default)')
    to_time = str(input('End Time: '))

    try:
        to_time = time.mktime(time.strptime(to_time, '%m/%d/%Y'))
    except:
        try:
            to_time = time.mktime(time.strptime(to_time, '%m/%d/%Y %H:%M:%S'))
        except:
            print('Invalid Time Format')
            exit()

    print('****************************')
    time_range = (from_time, to_time)

    return time_range
