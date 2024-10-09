# write a function that returns the pig latin version of a sentence
# For words that begin with a vowel (a, e, i, o, u), add "way".
# Otherwise, move all letters before the first vowel to the end and add "ay".
# For simplicity, no punctuation will be present in the inputs.

def pig_latin(str):
    """A function that returns the pig latin version of a sentence.
    >>> pig_latin("this is pig latin")
    'isthay isway igpay atinlay'

    >>> pig_latin("wall street journal")
    'allway eetstray ournaljay'
    """
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    str = str.lower().split()
    new_string = ''

    def flip_at_vowel(s):
        new_s = s
        for i in s:
            if i in vowels:
                return new_s
            else:
                temp = i
                new_s = new_s.replace(i, '', 1)
                new_s += temp

    for word in str:
        if word[0] in vowels:
            new_word = word + 'way'
        else:
            new_word = flip_at_vowel(word) 
            new_word += 'ay'
        new_string += ' ' + new_word

    return new_string.strip()

