def checkMagazine(magazine, note):
    '''
    He cannot use substrings or concatenation to create the words he needs.
    Given the words in the magazine and the words in the ransom note, 
    print Yes if he can replicate his ransom note exactly using whole words from the magazine; 
    otherwise, print No.

    magazine: an array of strings, each a word in the magazine
    note: an array of strings, each a word in the ransom note   
    '''

    d = {}
    for word in magazine:
        d.setdefault(word, 0)
        d[word] +=1
    
    for word in note:
        if word in d:
            d[word]-=1
        else:
            return False
    
    return 'Yes' if all([x>=0 for x in d.values()]) else 'No'

def check_rans(magazine, note):
    from collections import Counter
    if (Counter(note) - Counter(magazine)) == {}:
        return ('Yes')
    else:
        return ('No')

def ransom_intersect(magazine, note):
    '''
    tHE PROBLEM WITH THIS METHOD IS THE INTERSECTION
    only returns unique values within a set!
    Thus this method will not work for a generic case containing
    multiple values for a given key
    '''
    collect_mag = magazine.split()
    collect_not = note.split()
    intersect = (list(set(collect_mag).intersection(set(collect_not))))
    return intersect, collect_not
    
x = "two times two is not four "
y = "two times two is four"

print(checkMagazine(x, y))
print(check_rans(x, y))
from collections import Counter
count = {k:v for k, v in Counter(x).items() if v > 2}
print(count)

print(ransom_intersect(x, y))