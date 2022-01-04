class Solution:
    def sieveOfEratosthenes1(self, n):
        multiples = []
        for i in range(2, n+1):
            if i not in multiples:
                print (i)
                for j in range(i*i, n+1, i):

                    multiples.append(j)
    def soe(self, n):
        prime = [True for i in range(n+1)]
        p = 2
        while (p * p <= n):
    
            # If prime[p] is not
            # changed, then it is a prime
            if (prime[p] == True):
    
                # Update all multiples of p
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1
    
        # Print all prime numbers
        for p in range(2, n+1):
            if prime[p]:
                print (p)

s = Solution()
import time
toc = time.perf_counter()
s.sieveOfEratosthenes1(100)
tic = time.perf_counter()
print(f'{tic-toc}')

toc = time.perf_counter()
s.soe(100)
tic = time.perf_counter()
print(f'{tic-toc}')
