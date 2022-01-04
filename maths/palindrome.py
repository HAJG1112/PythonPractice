class Solution:
    def isDigitSumPalindrome(self,N):
        x = [int(a) for a in str(N)]
        num = sum(x)
        rev = [int(a) for a in str(num)]
        if rev[::-1] == rev:
            return 1
        else:
            return 0