def minimumBribes(q):
    '''
    q is an array of integers
    '''

    moves = 0  #initialize number of moves

    q = [P -1 for P in q]  #decrease q by 1 to make index matching more intuitive

    #loop through each person(P) in the queue(q)
    for i, P in enumerate(q):

        #check if any P is more than two placesahead of its original position
        if P - i > 2:
            print("Too chaotic")
            return
        
        #now we check whether P has received a bribe by looking at those ahead of P
        #since lowest value of P is 1, reindex the ting
        for j in range(max(P-1, 0), i):
            if q[j] > P:
                moves+=1
    print(moves)