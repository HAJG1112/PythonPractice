def makeAnagram(str1, str2):
    '''
    Given two strings,  and , that may or may not be of the same length, 
    determine the minimum number of character deletions required to make  and  anagrams. 
    Any characters can be deleted from either of the strings.
    For example, if  and , we can delete  from string  and  from string  so that both remaining 
    strings are  and  which are anagrams.
    '''
    dict_chars = dict()
    
    #for each character in the first string
    for char in str1:
        #add unique characters to the dictionary above
        if char in dict_chars:
            dict_chars[char] += 1
        else:
            dict_chars[char] = 1

    for char in str2:
        #add unique characters to the dictionary above
        if char in dict_chars:
            dict_chars[char] -= 1
        else:
            dict_chars[char] = -1
    
    sum_diff = 0
    
    #for each unique character in dict_chars
    for char in dict_chars.keys():
        sum_diff += abs(dict_chars[char])

    return sum_diff
    
a = "aadaevevyjyh"
b = "svbthaaaiwyhjk"

print(makeAnagram(a, b))