class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        row = len(strs)
        col = len(strs[0])
        
        delete = 0
        for i in range(col):
            current = strs[0][i]
            for j in range(1, row):
                if current > strs[j][i]:
                    delete += 1
                    break
                current = strs[j][i]
        return delete
