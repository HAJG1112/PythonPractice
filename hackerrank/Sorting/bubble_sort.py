def countSwaps(a):
    '''
    a is an array
    return the number of swaps to sort the array into ascending order
    via the bubble sort method
    '''
    count  = 0

    for iter_num in range(len(a) -1, 0, -1):
        for idx in range(iter_num):
            if a[idx]>a[idx+1]:
                temp = a[idx]
                a[idx] = a[idx+1]
                a[idx+1] = temp
                count+=1

    str1 = f"Array is sorted in {count} swaps"
    str2 = f"First Element: {a[0]}"
    str3 = f"Last Element: {a[-1]}"
    print(str1)
    print(str2)
    print(str3)

(countSwaps([3,2,1]))