def twoStrings(s1, s2):
    return list(set(s1) & set(s2))
        

print(twoStrings('hello', 'goodbye'))