class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        len_smallest_str = min([len(s) for s in strs])
        size_of_strs = len(strs)
        length_of_lcp = 0 # length of the longest common prefix
        
        # Check the first character of each string, 
        # if all are similar, increament length_of_lcp by one 
        # then repeat the same process with the next character of each string 
        for i in range(len_smallest_str):
            char_of_first_word = strs[0][i]
            
            for j in range(size_of_strs):
                if strs[j][i] != char_of_first_word:
                    # if any different character occured, return the answer
                    return strs[0][:length_of_lcp]
            length_of_lcp += 1
        
        return strs[0][:length_of_lcp]
