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
                    result = temp
            length -= 1
        return result

    def is_palindromic(self, s):
        return s == s[::-1]
