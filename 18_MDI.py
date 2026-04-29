class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        rev = 0
        x = n
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
        return abs(n - rev)