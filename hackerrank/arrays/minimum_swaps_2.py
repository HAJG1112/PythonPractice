def minimumSwaps(list):
    '''
    given an unsorted list, sort in in ascedning and print the number of swaps in the list
    it tok for the list to become sorted
    This relies on using the bubble sort algorithm

    This isn't the correct answer but it does the thing they are asking for?
    '''
    count = 0
    for iter_num in range(len(list)-1,0,-1):
            for idx in range(iter_num):
                if list[idx]>list[idx+1]:
                    temp = list[idx]
                    list[idx] = list[idx+1]
                    list[idx+1] = temp
                    count +=1
    return count

arr = [4,3,1,2]
print(minimumSwaps(arr))
print(arr)