# create a function that takes a list of numbers and returns a list
# with the items from the original list stored in sub lists
# items of the same value should be in the same sub list

def advanced_sort(list):
    terms = {}
    final = []

    # create a count of each term as it appears in the list
    for i in range(len(list)):
        if list[i] in terms:
            terms[list[i]].append(list[i])
        else:
            terms[list[i]] = [list[i]]

    for key in terms:
        final.append(terms[key])
    
    return final
    

a = [2, 1, 2, 1]
b = [5, 4, 5, 5, 4, 3]
c = ["b", "a", "b", "a", "c"]

print(advanced_sort(a))
print(advanced_sort(b))
print(advanced_sort(c))

    
