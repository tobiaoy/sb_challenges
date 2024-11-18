# Create a function that converts 12-hour time to 24-hour time or vice versa. Return the output as a string.

def convert_time(time):
    """
    A 12-hour time input will be denoted with an am or pm suffix.
    A 24-hour input time contains no suffix.
    >>> convert_time("12:00 am")
    '0:00'
    >>> convert_time("6:20 pm")
    '18:20'
    >>> convert_time("21:00")
    '9:00 pm'
    >>> convert_time("5:05")
    '5:05 am'
    """

    # time with a suffix
    if len(time) > 5:
        # time in the morning
        if time[-2] == 'a':
            if time.split(':')[0] == '12':
                return '0:00'
            else:
                return time[:-3]
        else:
            just_time = time[:-3]
            hour = just_time.split(':')[0]
            minute = just_time.split(':')[1]
            new_hour = str(int(hour) + 12)
            return new_hour + ':' + minute
    else:
        hour = time.split(':')[0]
        minute = time.split(':')[1]
        if int(hour) > 12:
            suffix = 'pm'
            new_hour = str(int(hour) - 12)
            return new_hour + ':' + minute + ' ' + suffix
        elif int(hour) <= 12:
            suffix = 'am'
            return hour + ':' + minute + ' ' + suffix

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)