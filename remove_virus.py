def remove_virus(string):
    """A function to remove files with viruses on them
    >>> remove_virus("PC Files: spotifysetup.exe, virus.exe, dog.jpg")
    'PC Files: spotifysetup.exe, dog.jpg'
    >>> remove_virus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe ")
    'PC Files: antivirus.exe, cat.pdf'
    >>> remove_virus("PC Files: notvirus.exe, funnycat.gif")
    'PC Files: notvirus.exe, funnycat.gif'
    """
    programs = string.split(':')[1]
    programs = programs.split(',')

    def contains_error(string):
        if ('notvirus' in string) or ('notmalware' in string) or ('antivirus' in string):
            return False
        elif ('virus' in string) or ('malware' in string):
            return True
    
    f_programs = []
    for p in programs:
        if not contains_error(p):
            f_programs.append(p)

    f_programs = ','.join(f_programs)
    if len(f_programs) > 0:
        output = 'PC Files:' + f_programs
    else:
        output = 'PC Files: Empty'
    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)



