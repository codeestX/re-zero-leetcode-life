class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        index = 0
        while len(s) is not 0:
            temp = list()
            for c in s:
                if c in temp:
                    index = s.find(c)
                    if len(temp) > result:
                        result = len(temp)
                    break
                else:
                    temp.append(c)
            if len(temp) == len(s) and len(temp) > result:
                result = len(temp)
            s = s[index + 1:len(s)]
            if len(s) < result:
                break
        return result
