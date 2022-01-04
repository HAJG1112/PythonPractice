def substrCount(n, s):
    '''
    A string is said to be a special string if either of two conditions is met:
    All of the characters are the same, e.g. aaa.
    All characters except the middle one are the same, e.g. aadaa.
    A special substring is any substring of a string which meets one of those criteria. 
    Given a string, determine how many special substrings can be formed from it.

    1. Build a list of tuples such that the string "aaabbc" can be squashed down to 
        [("a", 3), ("b", 2), ("c", 1)]. 
    2. add to answer all combinations of substrings from these tuples which would represent 
        palindromes which have all same letters. 
    3. traverse this list to specifically find the second case mentioned in the problem
    '''
    l = []
    count = 0
    cur = None
    # 1st pass
    for i in range(n):
        if s[i] == cur:
            count+=1
        else:
            if cur is not None:
                l.append((cur, count))
            cur = s[i]
            count = 1
    l.append((cur, count))
    ans = 0

    #2nd pass
    for i in l:
        ans += (i[1] * (i[1] + 1)) // 2

    # 3rd pass
    for i in range(1, len(l) - 1):
        if l[i - 1][0] == l[i + 1][0] and l[i][1] == 1:
            ans += min(l[i - 1][1], l[i + 1][1])

    return ans