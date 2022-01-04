# Given the first 2 terms A1 and A1 of an atrithmetic series. Find the Nth term of the series
class Solution:
    def nthTermOfAP(self, A1, A2, N):
        diff = A2 - A1  
        to_go = N*diff
        print(A1 + to_go)

if __name__ == '__main__':
    s = Solution()
    s.nthTermOfAP(2,3,5)