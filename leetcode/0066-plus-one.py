class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join([str(digit) for digit in digits])) + 1
        digits = [int(digit) for digit in str(num)]
        return digits
