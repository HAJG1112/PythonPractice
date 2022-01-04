def maxMin(k, arr):
    '''
    You will be given a list of integers, arr , and a single integer k. 
    You must create an array of length k from elements of arr such that its
    unfairness is minimized. 
    Call that array. Unfairness of an array is calculated as max(subarr) - min(subarr)
    
    1. Create a list of all possible sub arrays of length k
    2. save a value for each array consisting of max(subarr) - min(subarr)
    '''
    arr.sort()
    return min([arr[x+k-1]-arr[x] for x in range(n-k+1)])

arr = 
maxMin(3,  arr)