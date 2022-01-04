def maximumToys(prices, k):
    '''
    prices: arr  prices of toys in list/array
    k: int  marks total amount of money
    for a given array and amount of money, maximize the number of toys mark can buy

    This method is "too slow" as it works better with smaller arrays due to the number of loops
    '''
    # this is a bubble sort and sorts the prices ascending
    for iter_num in range(len(prices) -1, 0, -1):
        for idx in range(iter_num):
            if prices[idx]>prices[idx+1]:
                temp = prices[idx]
                prices[idx] = prices[idx+1]
                prices[idx+1] = temp
    
    # now these are sorted, and we cannot buy an item more than once we can add from left->right
    total = []  # initialise empty list to add summed basket price to
    idx = 0
    for i in range(1,len(prices)+1): #start index from 1
        if sum(prices[0:i]) <= k:
           idx = i 
    # now search the total list for a value less than k and return its position in the list
    # this means the index of total corresponds to the amount of items bought
    return(idx)

def maximumToys_1(prices, k):
    prices.sort()
    count = 0
    for i in prices:
        if (i <= k):
            count += 1
            k -= i
        else:
            break
    return count              

prices= [1, 12, 5, 111, 200, 1000, 10]
k = 50

print(maximumToys_1(prices, k))
