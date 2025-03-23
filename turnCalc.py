# Given a number, create a function that converts it into a word by turning the integer 180 degrees around.

def turnCalc (num):
    """
    Given a number, create a function that converts it into a word by turning the integer 180 degrees around.
    >>> turnCalc('707')
    'LOL'
    >>> turnCalc('5508')
    'BOSS'
    >>> turnCalc('3045')
    'SHOE'
    >>> turnCalc('07734')
    'HELLO'
    """

    # dictionary for the cypher
    cypher = {
        '1': 'I',
        '2': 'Z',
        '3': 'E',
        '4': 'H',
        '5': 'S',
        '6': 'G',
        '7': 'L',
        '8': 'B',
        '9': '-',
        '0': 'O',
        '.': '' 
    }

    num_list = list(num)
    for i in range(len(num_list)):
        num_list[i] = cypher[num_list[i]]
    
    output = ''.join(num_list)
    return output[::-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)