'''
The Question:
Create a route exists method that returns true if the destination is reachable and false if it is not. 
The first 2 parameters denote the starting x and y respectively, and the second two parameters denote
the ending x and y respectively. The roads on the map are rasterized and produce a matrix of boolean values 
- True if the road is present and False otherwise. Roads in the matrix are only connected if the road is immediately
left, right, below or above it.
'''
matrix = [[True, False, False, False],
         [True, True, False, False],
         [False, True, True, False],
         [False, False, True, True]]


def route_exists(start_x, start_y, end_x, end_y, map_matrix):
    import numpy as np
    is_route = False
    tuple_list = [i for i in np.ndenumerate(map_matrix)]  #returns list object of location and corresponding boolean
    len_list = len(tuple_list)    
    route_list = []  #empty list to attach True routes

    for x in range(len_list):

        for i in range(len(map_matrix)):  #for each row fro starting x and ending x

            for j in range(len(map_matrix)): #for each column ofr starting y and ending y

                loc = (tuple_list[x][0])  #matrix lcoation of tuple
                if loc == (i,j) and tuple_list[x][1]==True:
                    route_list.append(tuple_list[x][0])
                    
                if loc==(end_x, end_y) and tuple_list[x][1]==True :
                    is_route = True
                else:
                    is_route = False

    return(is_route, route_list)


print(route_exists(0,0,3,3,matrix))

