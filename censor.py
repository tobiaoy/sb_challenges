# Create a function that takes a string and censors words over four characters with *

def censor(string):
    """ A function that takes a string and censors worss over 4 characters 
    >>> censor("The code is fourty")
    'The code is ******'
    >>> censor("Two plus three is five")
    'Two plus ***** is five'
    >>> censor("aaaa aaaaa 1234 12345")
    'aaaa ***** 1234 *****'
    """
    txt = string.split()

    def make_stars(n):
        stars = ""
        for i in range(n):
            stars = stars + "*"
        return stars

    n = len(txt)
    for i in range(n):
        if len(txt[i]) > 4:
            txt[i] = make_stars(len(txt[i]))
    
    result = " ".join(txt)
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)