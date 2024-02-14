class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_consecutive = 0
        max_consecutive = 0
        for b in nums:
            if b:
                current_consecutive += 1
            else:
                if current_consecutive > max_consecutive:
                    max_consecutive = current_consecutive
                current_consecutive = 0
        if current_consecutive > max_consecutive:
            max_consecutive = current_consecutive
        return max_consecutive
        
