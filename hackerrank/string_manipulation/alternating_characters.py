def alternatingCharacters(s):
    '''
    Given a string containing A and B only. Task is to change the string so that there are no 
    mathcing adjacent characters. 
    To do this you are allowed to delete zero or more characters in the string
    Task is to find the minimum number of deleteions.

    idea: simply loop through the string and follow these two rules
    if char == char+1 
    increase the count, we dont need to actually delete, just count the amount of deletions

    ''' 
    count = 0
    for num in range (len(s)-1):
        if s[num] == s[num+1]:
            count +=1
    return count

print(alternatingCharacters("ABBAABABA"))