# Given a number of petals, return a string which repeats the phrases "Loves me" and "Loves me not" for every alternating petal, and return the last phrase in all caps. Remember to put a comma and space between phrases.

def is_even(num):
    if num == 0:
        return True
    if num % 2 == 0:
        return True
    else:
        return False
    
def loves_me(num):
    string = []
    for n in range(num):
        if is_even(n):
            string.append('Loves me')
        else:
            string.append('Loves me not')

    string[-1] = string[-1].upper()
    return ', '.join(string)

print(loves_me(3))
print(loves_me(6))
print(loves_me(1))
