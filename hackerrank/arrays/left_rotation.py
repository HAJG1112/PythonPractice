def rot_left(arr, d):
    '''
    arr : type(int) refers to a parsed array of integers a
    d : type(int) refers to the number of rotations

    constraints
    1<=n<=10**5
    1<=d<=n
    1<=a[i]<=10**6
    '''
    arr = [x for x in range(1, arr+1)]
    temp = []
    for i in range(d):
        x = arr.pop(0) #retrieve first value
        arr.append(x)
    return arr


print(rot_left(5, 4))
