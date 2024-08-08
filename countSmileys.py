# Create a function that takes an array of strings and return the number of smiley faces contained within it. These are the components that make up a valid smiley:
# A smiley has eyes. Eyes can be : or ;
# A smiley has a nose but it doesn't have to. A nose can be - or ~
# A smiley has a mouth which can be ) or D

def countSmileys(arr):
    count = 0
    
    if len(arr) == 0:
        return 0
    
    for em in arr:
        if len(em) == 3:
            if (em[0] == ':' or em[0] == ';') and (em[1] == '-' or em[1] == '~') and (em[2] == 'D' or em[2] == ')'):
                count += 1
        elif len(em) == 2:
            if (em[0] == ':' or em[0] == ';') and (em[1] == ')' or em[1] == 'D'):
                count += 1
    
    return count

a = countSmileys([":)", ";(", ";}", ":-D"])
b = countSmileys([";D", ":-(", ":-)", ";~)"])
c = countSmileys([";]", ":[", ";*", ":$", ";-D"])

print(a)
print(b)
print(c)


