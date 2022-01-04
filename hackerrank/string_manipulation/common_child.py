def commonChild(a, b):
    '''
    A string is said to be a child of a another string if it can be formed by deleting 0 
    or more characters from the other string. Given two strings of equal length, 
    what's the longest string that can be constructed such that it is a child of both?

    print s that is a child of both s1 and s2
    '''

    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = \
                    max(lengths[i+1][j], lengths[i][j+1])
     
    return lengths[-1][-1]

print(commonChild("HARRY", "SALLY"))