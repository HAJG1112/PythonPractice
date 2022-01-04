import sys
sys.setrecursionlimit(1500)
import math
def count(a):
    counter  = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if i!=j:
                if (a[i] + a[j]) % 60 == 0:
                    counter +=1
    return counter/2

print(count([4,10,50,90,30]))