def isValid(s):
    '''
    Sherlock considers a string to be valid if 
    all characters of the string appear the same number of times
    It is also valid if he can remove just  character at  index in the string, 
    and the remaining characters will occur the same number of times. 
    Given a string , determine if it is valid. 
    If so, return YES, otherwise return NO.
    '''
    from collections import Counter
    s = s.lower()
    s = Counter(s) #count number of unique characters
    cs = Counter(s.values()) #group number of counts of each character.

    if len(cs.keys())==1:
        print("YES")

    elif len(cs.values())==2:
        key1, key2=cs.keys()
        if cs[key1]==1 and (key1-1==key2 or key1-1==0):
            print("YES")
        elif cs[key2]==1 and (key2-1==key1 or key2-1==0):
            print("YES")
        else:
            print("NO")

    else:
        print("NO")

isValid("asfccf")