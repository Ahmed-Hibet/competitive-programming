from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) // 3
        nums = Counter(nums)
        nums = [key for key in nums if nums[key] > threshold]
        return nums
