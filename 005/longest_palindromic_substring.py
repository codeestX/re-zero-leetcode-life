class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = s[0:1]
        length = len(s)
        while length > 0:
            for i in range(0, len(s) - length + 1):
                temp = s[i:i + length]
                if self.is_palindromic(temp) and len(temp) > len(result):
                    return temp
            length -= 1
        return result

    def is_palindromic(self, s):
        if len(s) == 0 or len(s) == 1:
            return True
        if s[:1] != s[-1:]:
            return False
        return self.is_palindromic(s[1:-1])
