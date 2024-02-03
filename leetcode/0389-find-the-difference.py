class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = sorted(s)
        t = sorted(t)
        len_s = len(s)

        for i in range(len_s):
            if s[i] != t[i]:
                return t[i]
        return t[-1]
