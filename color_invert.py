def color_invert(color):
    """A function to invert any rgb color. 
    >>> color_invert([0, 0, 0])
    [255, 255, 255]
    >>> color_invert([165, 170, 221])
    [90, 85, 34]
    """
    return [255 - x for x in color]

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)