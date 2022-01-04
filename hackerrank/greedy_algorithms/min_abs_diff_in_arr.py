
def minimumAbsoluteDifference(arr):
    # key is to sort the algorithm first
    # Time complexity is (O(n))
    n = len(arr)
    s = sorted(arr)
    diff = []
    for i in range(0,len(s)-1):
            diff.append(abs(s[i] - s[i+1]))
    return min(diff)




arr = [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]
print(minimumAbsoluteDifference(arr))