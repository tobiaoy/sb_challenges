# valid phone num - (123) 456-7890
# rules - in 0 > '('; in 4 > ')'; 5 > ' '; 9 > '-' ; length - 14

def is_valid_phone_number (num):
    """ A function to check if a number is a valid phone number
    >>> is_valid_phone_number("(123) 456-7890")
    True
    >>> is_valid_phone_number("1111)555 2345")
    False
    >>> is_valid_phone_number("098) 123 4567")
    False
    """
    if len(num) != 14:
        return False
    if num[0] == '(' and num[4] == ')' and num[5] == ' ' and num[9] == '-':
        return True
    else:
        return False
    

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)