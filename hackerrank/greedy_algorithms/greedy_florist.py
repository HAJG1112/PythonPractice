def getMinimumCost(k, c):
    '''
    A group of friends want to buy a bouquet of flowers. 
    The florist wants to maximize his number of new customers and the money he makes. 
    To do this, he decides he'll multiply the price of each flower by the number of 
    that customer's previously purchased flowers plus 1.

    '''
    n = len(c)
    c = sorted(c, reverse= True)
    cost = 0

    for i in range(0,n):
        cost+=(i//k + 1) *c[i]
    return cost


c = [1, 2, 7, 9, 100]
k =2
print(getMinimumCost(k, c))