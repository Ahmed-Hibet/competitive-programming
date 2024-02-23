class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ones = len([1 for num in nums if num])
        zeros = 0

        for i in range(n):
            if nums[i]:
                nums[i] = zeros + ones
                ones -= 1
            else:
                nums[i] = zeros + ones
                zeros += 1
        nums.append(zeros+ones)

        max_score = max(nums)
        result = [i for i in range(n+1) if nums[i] == max_score]
        return result

