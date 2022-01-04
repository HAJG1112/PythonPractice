def hourglassSum(arr):

    
    sums = -64
    #create an hourglass function as a loc slice of a given matrix
    #need conditions that limits the iterated length of the hourglass wrt 
    # the matrix size
    temp = []
    for i in range(len(arr) - 2):
        for j in range(len(arr[0]) - 2):
                tot = (arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2])
                temp.append(tot)
    return max(temp)

import numpy as np
arr = np.array( [[1, 1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [0, 0, 2, 4, 4, 0],
                [0, 0, 0, 2, 0, 0],
                [0, 0, 1, 2, 4, 0]])

print(hourglassSum(arr))