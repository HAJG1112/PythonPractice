def activityNotifications(exp, d):
    '''
    expenditure: an array of integers representing daily expenditures
    d: an integer, the lookback days for median spending

    The problem with this is how it handles the "median" value
    '''
    import statistics
    # Notification count
    notify = 0

    # Check if trailing days != 
    #if d < len(exp):

    lead = exp[d:]

    for i in range(len(lead)):

        # Calculate median
        med = statistics.median(exp[i:d+i])

        if (lead[i] >= 2*med):

            notify += 1

    return notify


expenditures = [10, 20, 30, 40, 50]
d = 3

print(activityNotifications(expenditures, d))