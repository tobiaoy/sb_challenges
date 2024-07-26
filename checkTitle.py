# check if something is a title or not

def checkTitle(str):
    original = str
    titled = str.title()

    if original == titled:
        return True
    else:
        return False
    
a = checkTitle("A Mind Boggling Achievement")
b = checkTitle("A Simple C++ Program!")
c = checkTitle("Water is transparent")

print(a)
print(b)
print(c)