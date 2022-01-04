class Solution:
    	def Nth_term(self, a, r, n):
		# Code here
            val = a*r**(n-1)
            return val

if __name__ == '__main__':
    s = Solution()
    print(s.Nth_term(5,9,10))