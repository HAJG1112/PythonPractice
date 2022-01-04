class Solution:
    def getTable(self, N):
        for i in range(1,11):
            print(i*N)

if __name__ == '__main__':
    s = Solution()
    s.getTable(5)