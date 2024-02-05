class Solution:
    def freqAlphabets(self, s: str) -> str:
        s = s[::-1]
        len_s = len(s)
        index = 0
        result = []

        while index < len_s:
            if s[index] == '#':
                char = chr(96 + int(s[index+2] + s[index+1]))
                index += 3
            else:
                char = chr(96 + int(s[index]))
                index += 1
        
            result.append(char)
        return ''.join(result[::-1])
