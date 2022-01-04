class Solution:
    def armstrongNumber (self, n):
        x = [int(a) for a in str(n)]
        val = sum([y**3 for y in x])
        if val == n:
            return 'Yes'
        else:
            return 'No'