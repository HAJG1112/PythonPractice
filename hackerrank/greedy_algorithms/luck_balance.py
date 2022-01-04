def luckBalance(k, contests):
    '''
    K: int -  amoubt of contests she can lose
    contest: (L, T)
    L: Luck value, if she loses L luck balance increase by L and vice versa
    T: 0 or 1. 1 if the contest is important 

    She cannot lose more than k important contests.
    '''
    luck = 0
    contests.sort(reverse=True)

    for contest in contests:
        if (contest[1] == 0): #if the contest is not important, we want to lose and gain luck
            luck += contest [0] #add the luck
        
        elif k > 0:   #if the number we can lose is greater than 0
            luck+= contest [0]
            k-=1 #reduce the number of loses we can take
        
        else:
            luck-=contest[0]  #if we win, reduce the amount of luck
            

    return luck


cont = [[6, 3],
        [5, 1],
        [2, 1],
        [1, 1],
        [8, 1],
        [10, 0],
        [5, 0]]

print(luckBalance(5, cont))