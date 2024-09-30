# You are given the length of a video in minutes. The format is mm:ss (ex: "02:54").
# Create a function that takes the video length and return it in seconds.
# we can take the ':' as a delimiter

def minutes_to_seconds(time):
    """Takes a string in mm:ss format and returns the amount of minutes.
    - does not allow ss to be > than 59
    - mm can be greater than 59

    >>> minutes_to_seconds("01:00")
    60
    >>> minutes_to_seconds("13:56")
    836
    >>> minutes_to_seconds("10:60")
    -1
    >>> minutes_to_seconds("121:49")
    7309
    """

    minutes = int(time.split(':')[0])
    seconds = int(time.split(':')[1])

    if seconds > 59:
        return -1
    else:
        return (minutes * 60) + seconds