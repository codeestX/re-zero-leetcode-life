class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        pos = 1 if x >= 0 else -1
        x = str(abs(x))[::-1]
        return int(x) * pos if int(x) <= pow(2, 31) else 0
