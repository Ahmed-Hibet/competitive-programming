class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        # let n is an integer, n + n+1 + n+2 = 3n + 3 = num
        if (num - 3) % 3 == 0:
            n = (num - 3) // 3
            return [n, n+1, n+2]
        return []
        
