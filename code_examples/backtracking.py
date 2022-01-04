def permute(length, s):
    if length == 1:
        return s
    else:
        return [ y + x
                 for y in permute(1, s)
                 for x in permute(length - 1, s)
                 ]

print(permute(2, ["a","b","c"]))
print(permute(5, ["H","T"]))
print(permute(2, [2,5,10]))
