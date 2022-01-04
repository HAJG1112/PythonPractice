'''As a part of the route planner, the route_exists method is used as a quick filter if the destination is reachable,
before using more computationally intensive procedures for finding the optimal route.

The roads on the map are rasterized and produce a matrix of boolean values
- True if the road is present or False if it is not.
The roads in the matrix are connected only if the road is immediately left, right, below or above it.

Finish the route_exists method so that it returns True if the destination is reachable or False if it is not.
The from_row and from_column parameters are the starting row and column in the map_matrix.
The to_row and to_column are the destination row and column in the map_matrix.
The map_matrix parameter is the above mentioned matrix produced from the map.

For example, for the given rasterized map, the code below should return True since the destination is reachable:
map_matrix = [
    [True, False, False],
    [True, True, False],
    [False, True, True]
];

route_exists(0, 0, 2, 2, map_matrix)
'''

'''
# Haisun's Solution

import numpy as np

def route_exists(start_x, start_y, end_x, end_y, map_matrix):

    is_route = False
    tuple_list = [i for i in np.ndenumerate(map_matrix)]  #returns list object of location and corresponding boolean
    len_list = len(tuple_list)    
    route_list = []  #empty list to attach True routes

    for x in range(len_list):

        for i in range(len(map_matrix)):  #for each row fro starting x and ending x

            for j in range(len(map_matrix[0])): #for each column ofr starting y and ending y

                loc = (tuple_list[x][0])  #matrix lcoation of tuple
                if loc == (i,j) and tuple_list[x][1]==True:
                    route_list.append(tuple_list[x][0])
                    
                if loc==(end_x, end_y) and tuple_list[x][1]==True:
                    is_route = True
                else:
                    is_route = False

    return(is_route, route_list)
                    
matrix = [[True, False, False, False],
         [True, True, False, False],
         [False, True, True, False],
         [False, False, True, False]]

print(matrix)

print(route_exists(0,0,3,2, matrix))
'''
import numpy as np
def route_exists(start_x, start_y, end_x, end_y, map_matrix):

    is_route = True

    map_col = len(map_matrix[0]) 
    map_row = len(map_matrix)

    tuple_list = [(index, x) for index, x in np.ndenumerate(map_matrix)]
    path_trial = []  #empty list to attach True routes
    
    path_trial.append((start_x, start_y)) # include the start point into the trail

    for n in range(len(tuple_list)):
        
        # HEADING SOUTH/ NORTH/ EAST / WEST
        if map_matrix[start_x][start_y] == True:  #if the starting coordinates are True

            #SOUTH
            if start_x + 1 < map_row and map_matrix[start_x + 1][start_y] == True and (start_x + 1, start_y) not in path_trial:
                start_x += 1
                path_trial.append((start_x, start_y))
            #NORTH
            elif start_x - 1 >= 0 and map_matrix[start_x - 1][start_y] == True and (start_x - 1, start_y) not in path_trial:
                start_x -= 1
                path_trial.append((start_x, start_y))
            #EAST
            elif start_y + 1 < map_col and map_matrix[start_x][start_y + 1] == True and (start_x, start_y + 1) not in path_trial:
                start_y += 1
                path_trial.append((start_x, start_y))
            #WEST
            elif start_y - 1 >= 0 and map_matrix[start_x][start_y - 1] == True and (start_x, start_y - 1) not in path_trial:
                start_y -= 1
                path_trial.append((start_x, start_y))
            else:
                (start_x, start_y) = (start_x, start_y)
                continue 
        else:
            (start_x, start_y) = (start_x, start_y)
            break
        
        
    if (start_x,start_y) == (end_x, end_y):
        is_route = True
    else:
        is_route = False

    return (is_route, path_trial)

if __name__ == '__main__':
    map_matrix = [
        [True, True, False],
        [True, True, False],
        [False, True, True],
        [True, True, False]
    ];

    print(route_exists(0, 0, 3, 3, map_matrix))
   