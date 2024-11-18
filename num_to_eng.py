# There are no hyphens used (e.g. "thirty five" not "thirty-five").
# The word "and" is not used (e.g. "one hundred one" not "one hundred and one").

def num_to_eng(num):
    """ A function that accepts a positive integer between 0 and 999 inclusive and returns a string representation of that integer written in English
    >>> num_to_eng(0)
    'zero'
    >>> num_to_eng(18)
    'eighteen'
    >>> num_to_eng(126)
    'one hundred twenty six'
    >>> num_to_eng(909)
    'nine hundred nine'
    """
    val = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred'    
        }
    
    if num < 0:
        return
    
    if num <= 20:
        return val[num]
    elif num < 100:
        ten = num // 10 * 10
        unit = num - ten
        if unit > 0:
            return val[ten] + ' ' + val[unit]
        else:
            return val[ten]
    else:
        hundred = num // 100 * 100
        ten = num % hundred
        if ten <= 20:
            return val[hundred // 100] + ' hundred ' + val[ten]
        else:
            current_ten = ten
            ten = current_ten // 10 * 10
            unit = current_ten - ten
            if ten > 0 and unit > 0:
                return val[hundred // 100] + ' hundred ' + val[ten] + ' ' + val[unit]
            elif ten > 0 and unit < 0:
                return val[hundred // 100] + ' ' + val[ten]
            else:
                return val[hundred // 100] + ' hundred ' + val[unit]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    