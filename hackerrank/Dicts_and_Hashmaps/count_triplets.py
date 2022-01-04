def countTriplets(arr, r): 
    map_arr = {}   
    map_doubles = {}
    count = 0
    if len(arr) <= 2:
        return (0)
    # Traversing the array from the rear, helps avoid division
    #instead we check if x[i-1] * r = x[i]
    for x in arr[::-1]:

        r_x = r*x
        r_r_x = r*r_x

        # case: x is the first element (x, x*r, x*r*r)
        count += map_doubles.get((r_x, r_r_x), 0)

        # case: x is the second element (x/r, x, x*r)
        map_doubles[(x,r_x)] = map_doubles.get((x,r_x), 0) + map_arr.get(r_x, 0)

        # case: x is the third element (x/(r*r), x/r, x)
        map_arr[x] = map_arr.get(x, 0) + 1
        
    return count

arr = [1, 3, 3, 9, 3, 27]
cr = 3

print(countTriplets(arr, cr))