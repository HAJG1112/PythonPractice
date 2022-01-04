

def sherlockAndAnagrams(s):
    from collections import Counter
    '''
    We find all possible subtrings of s using the following loop
    for i in range(1,len(s)):
        for j in range(0,len(s)-i+1):
        print(s[j:j+i],end=", ")
    '''
    count = Counter(("".join(sorted(s[j:j+i])) for i in range(1,len(s)) for j in range(0,len(s)-i+1) ))
    return sum(sum(range(i)) for i in count.values())

def ret_substrings(s):
    from collections import Counter
    #print(Counter(s))
    count = {k:v for k, v in Counter(s).items() if v>1}
    #print(count)
    for i in range(1,len(s)):
        for j in range(0,len(s)-i+1):
            print(s[j:j+i],end=", ")

print(sherlockAndAnagrams("haivndhhhhv"))
print(ret_substrings("haivndhhhhv"))