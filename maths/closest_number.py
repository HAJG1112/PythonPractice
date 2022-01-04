class Solution:
    def closestNumber(self, n , m):
        # Find the quotient
        q = int(n / m)
        
        # 1st possible closest number
        n1 = m * q
        
        # 2nd possible closest number
        if((n * m) > 0) :
            n2 = (m * (q + 1))
        else :
            n2 = (m * (q - 1))
        
        # if true, then n1 is the required closest number
        if (abs(n - n1) < abs(n - n2)) :
            return n1
        
        # else n2 is the required closest number
        return n2

if __name__ == '__main__':
    s = Solution()
    print(int(5/3))
    print(s.closestNumber(-31764, 6540))