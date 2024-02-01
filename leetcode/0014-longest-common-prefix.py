class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        mn = min([len(s) for s in strs])
        n = len(strs)
        index = 0
        for i in range(mn):
            ch = strs[0][i]
            for j in range(n):
                if strs[j][i] != ch:
                    return strs[0][:index]
            index += 1
        return strs[0][:index]
