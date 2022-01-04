import numpy as np
c = 0.035
t = np.arange(0.5,5.5,0.5)
ytm =  0.01
M = 1350
FV = 1000
BP = 1000

print(t)
val = 0
for i in range(len(t)):
    val +=  (t[i]*c) / ((1+ytm)**t[i])   
fin = val + ((t[-1]*FV)/(1+ytm)**t[-1])

print(fin/1350)