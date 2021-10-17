import time


def get_input() -> tuple:
    from_time = str(
        input('Please set start time in the following format\nmm/dd/yyyy or mm/dd/yyyy HH:MM:SS\nStart Time: '))

    try:
        from_time = time.mktime(time.strptime(from_time, '%m/%d/%Y'))
    except:
        try:
            from_time = time.mktime(time.strptime(from_time, '%m/%d/%Y %H:%M:%S'))
        except:
            print('Invalid Time Format')
            exit()

    print('****************************')

    to_time = str(input('Please set end time in the following format\nmm/dd/yyyy or mm/dd/yyyy HH:MM:SS\nEnd Time: '))

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
